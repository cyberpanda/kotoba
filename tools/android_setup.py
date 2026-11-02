#!/usr/bin/env python3
"""Run once after `npx tauri android init` (make android-init does it for you).

* copies the 言 launcher icons into the Android project
* adds release signing that reads src-tauri/gen/android/keystore.properties (if present)
* dark window background + all orientations, phone/tablet/foldable friendly (resizeableActivity)
"""
import glob, os, re, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AND = os.path.join(ROOT, "src-tauri", "gen", "android")
if not os.path.isdir(AND):
    raise SystemExit("src-tauri/gen/android not found – run `npx tauri android init` first.")

res = os.path.join(AND, "app", "src", "main", "res")
src = os.path.join(ROOT, "src-tauri", "icons", "android")
for d in os.listdir(src):
    os.makedirs(os.path.join(res, d), exist_ok=True)
    for f in os.listdir(os.path.join(src, d)):
        shutil.copy(os.path.join(src, d, f), os.path.join(res, d, f))
print("icons ->", os.path.relpath(res, ROOT))

gradle = os.path.join(AND, "app", "build.gradle.kts")
SIGN = '''
    signingConfigs {
        create("release") {
            val keystorePropertiesFile = rootProject.file("keystore.properties")
            if (keystorePropertiesFile.exists()) {
                val keystoreProperties = java.util.Properties()
                keystoreProperties.load(java.io.FileInputStream(keystorePropertiesFile))
                keyAlias = keystoreProperties["keyAlias"] as String
                keyPassword = keystoreProperties["password"] as String
                storeFile = file(keystoreProperties["storeFile"] as String)
                storePassword = keystoreProperties["password"] as String
            }
        }
    }
'''
if os.path.exists(gradle):
    g = open(gradle).read()
    if 'create("release")' not in g:
        g = g.replace("    buildTypes {", SIGN + "    buildTypes {", 1)
        g = re.sub(r'(getByName\("release"\)\s*\{)', r'\1\n            if (rootProject.file("keystore.properties").exists()) signingConfig = signingConfigs.getByName("release")', g, count=1)
        open(gradle, "w").write(g)
        print("release signing added to", os.path.relpath(gradle, ROOT))
else:
    print("note: app/build.gradle.kts not found – add signing manually (see docs/BUILD.md)")

for man in glob.glob(os.path.join(AND, "app", "src", "main", "AndroidManifest.xml")):
    m = open(man).read()
    if "resizeableActivity" not in m:
        m = m.replace("<activity", '<activity\n            android:resizeableActivity="true"', 1)
    m = re.sub(r'\s*android:screenOrientation="[^"]*"', "", m)
    open(man, "w").write(m)
    print("patched", os.path.relpath(man, ROOT))

print("Android project ready:  npx tauri android dev   |   make apk   |   make aab")
