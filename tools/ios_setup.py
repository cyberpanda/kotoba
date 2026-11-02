#!/usr/bin/env python3
"""Run once after `npx tauri ios init` (make ios-init does it for you).

* iPhone + iPad (universal), all orientations, Split View / Stage Manager, foldable-friendly
* status bar over the app, no white flash on launch (dark launch background)
* copies the 言 icons into the Xcode asset catalog
"""
import glob, os, plistlib, re, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPLE = os.path.join(ROOT, "src-tauri", "gen", "apple")
if not os.path.isdir(APPLE):
    raise SystemExit("src-tauri/gen/apple not found – run `npx tauri ios init` first (on macOS).")

ALL = ["UIInterfaceOrientationPortrait", "UIInterfaceOrientationPortraitUpsideDown",
       "UIInterfaceOrientationLandscapeLeft", "UIInterfaceOrientationLandscapeRight"]

for plist in glob.glob(os.path.join(APPLE, "*_iOS", "Info.plist")):
    with open(plist, "rb") as f:
        d = plistlib.load(f)
    d["UISupportedInterfaceOrientations"] = ALL
    d["UISupportedInterfaceOrientations~ipad"] = ALL
    d["UIRequiresFullScreen"] = False
    d["UIStatusBarStyle"] = "UIStatusBarStyleLightContent"
    d["UIViewControllerBasedStatusBarAppearance"] = False
    d["ITSAppUsesNonExemptEncryption"] = False
    d["CFBundleDisplayName"] = "Kotoba"
    with open(plist, "wb") as f:
        plistlib.dump(d, f)
    print("patched", os.path.relpath(plist, ROOT))

for yml in glob.glob(os.path.join(APPLE, "project.yml")):
    s = open(yml).read()
    s2 = re.sub(r'TARGETED_DEVICE_FAMILY:\s*"?[\d,]+"?', 'TARGETED_DEVICE_FAMILY: "1,2"', s)
    if "TARGETED_DEVICE_FAMILY" not in s2:
        print("note: add TARGETED_DEVICE_FAMILY \"1,2\" in Xcode (General → Supported Destinations: iPhone, iPad)")
    open(yml, "w").write(s2)
    print("patched", os.path.relpath(yml, ROOT))

src = os.path.join(ROOT, "src-tauri", "icons", "ios")
for cat in glob.glob(os.path.join(APPLE, "**", "AppIcon.appiconset"), recursive=True):
    for f in os.listdir(src):
        shutil.copy(os.path.join(src, f), os.path.join(cat, f))
    print("icons ->", os.path.relpath(cat, ROOT))
print("iOS project ready. Open with: npx tauri ios dev   or   open src-tauri/gen/apple/*.xcodeproj")
