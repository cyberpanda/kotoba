# Building the native apps

One code base → **iOS/iPadOS, Android, macOS, Windows, Linux** via [Tauri 2](https://v2.tauri.app).
The app window shows the same `dist/web` build that runs in the browser, using the system web view
(WKWebView on Apple, WebView2 on Windows, WebKitGTK on Linux) – small downloads (≈ 5–15 MB), no
bundled browser.

| Target | Build on | Output |
|---|---|---|
| macOS (universal) | your Mac | `.app`, `.dmg` |
| iOS / iPadOS | your Mac (Xcode) | `.ipa` (App Store / TestFlight / ad hoc) |
| Windows x64 | GitHub Actions (or a Windows PC) | NSIS `-setup.exe`, `.msi` |
| Linux x64 | GitHub Actions (or Linux) | `.AppImage`, `.deb`, `.rpm` |
| Android (phone, tablet, foldable) | your Mac (Android Studio) or GitHub Actions | `.apk` (direct), `.aab` (Google Play) |

You only have a Mac? Build macOS + iOS locally and let the **Release** workflow build Windows and
Linux (see [RELEASING.md](RELEASING.md)).

---

## 1. One-time setup on macOS

```bash
xcode-select --install                    # command line tools
# Xcode from the App Store (for iOS), open it once and accept the license
brew install node python@3.12             # Node 20+ and Python 3
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh    # Rust
brew install cocoapods                    # needed by Tauri iOS
git clone <your-repo> kotoba && cd kotoba
npm install                               # installs the Tauri CLI locally
```

Check: `npx tauri info` should list Xcode, Rust and the targets without errors.

## 2. macOS app

```bash
make mac
# = rustup target add aarch64-apple-darwin x86_64-apple-darwin
#   npx tauri build --target universal-apple-darwin
```

Output: `src-tauri/target/universal-apple-darwin/release/bundle/{macos/Kotoba.app, dmg/Kotoba_2.0.0_universal.dmg}`

Run during development: `npx tauri dev`.

### Signing & notarization (to ship outside your own Mac)

Unsigned apps open on your Mac; other users get a Gatekeeper warning. For distribution:

1. Apple Developer Program → certificate **Developer ID Application** → install in Keychain.
2. Export before building:

```bash
export APPLE_SIGNING_IDENTITY="Developer ID Application: Your Name (TEAMID)"
export APPLE_ID="you@example.com"
export APPLE_PASSWORD="app-specific-password"   # appleid.apple.com → App-Specific Passwords
export APPLE_TEAM_ID="TEAMID"
make mac          # Tauri signs and notarizes automatically
```

For CI add the same values as repository secrets (plus `APPLE_CERTIFICATE` = base64 of the exported
`.p12` and `APPLE_CERTIFICATE_PASSWORD`).

## 3. iPhone & iPad (.ipa)

```bash
make ios-init      # once – creates src-tauri/gen/apple (Xcode project) and runs tools/ios_setup.py
```

`tools/ios_setup.py` configures the project for **iPhone and iPad** (universal), all
orientations, Split View / Slide Over / Stage Manager (not full-screen-only, so it adapts to
foldables and any window size), light status bar, and copies the 言 app icons.
Commit `src-tauri/gen/apple` afterwards.

Signing: open Xcode once (`open src-tauri/gen/apple/*.xcodeproj`) → target *kotoba_iOS* →
*Signing & Capabilities* → choose your **Team** (free Apple ID works for your own devices; App Store
needs the paid program). Or set `export APPLE_DEVELOPMENT_TEAM=TEAMID`.

```bash
make ios-dev       # simulator or a connected iPhone/iPad (pick in the prompt)
make ipa           # App Store / TestFlight .ipa  → src-tauri/gen/apple/build/arm64/Kotoba.ipa
make ipa-adhoc     # .ipa for registered test devices
```

Upload to TestFlight: **Transporter** app (drag the `.ipa`) or
`xcrun altool --upload-app -f Kotoba.ipa -t ios --apiKey KEY --apiIssuer ISSUER`.

App Store checklist: bundle id `app.cyberpanda.kotoba` (change `identifier` in
`src-tauri/tauri.conf.json` to your own reverse domain *before* `ios-init`), privacy: “Data not
collected”, age rating 4+, screenshots from `docs/screenshots` or the simulator.

## 4. Windows (.exe) and Linux (.AppImage)

Easiest: push a tag – GitHub Actions builds them (`.github/workflows/release.yml`).

Locally on Windows: install Rust, Node, Python, *Visual Studio Build Tools (C++)*, then `npm install && npx tauri build`
→ `src-tauri/target/release/bundle/nsis/Kotoba_2.0.0_x64-setup.exe`.

Locally on Linux (Ubuntu 22.04+):

```bash
sudo apt install libwebkit2gtk-4.1-dev libappindicator3-dev librsvg2-dev patchelf build-essential
npm install && npx tauri build      # → bundle/appimage/Kotoba_2.0.0_amd64.AppImage, deb, rpm
```

## 5. Android (.apk / .aab)

One-time setup on the Mac:

1. Install **Android Studio** → *More Actions → SDK Manager*: Android SDK Platform (latest),
   *SDK Tools*: **NDK (Side by side)**, Android SDK Command-line Tools.
2. Add to `~/.zshrc`:

```bash
export JAVA_HOME="/Applications/Android Studio.app/Contents/jbr/Contents/Home"
export ANDROID_HOME="$HOME/Library/Android/sdk"
export NDK_HOME="$ANDROID_HOME/ndk/$(ls -1 $ANDROID_HOME/ndk | tail -1)"
```

3. Create the project (once) – also copies the icons, enables free resizing for tablets/foldables
   and prepares release signing:

```bash
make android-init     # = rustup targets + npx tauri android init + tools/android_setup.py
```

Commit `src-tauri/gen/android` afterwards.

Build & run:

```bash
make android-dev      # emulator or USB device (enable USB debugging)
make apk              # → src-tauri/gen/android/app/build/outputs/apk/universal/release/*.apk
make aab              # → …/bundle/universalRelease/*.aab  (upload to Google Play Console)
```

### Signing (needed to install a release APK / publish on Play)

```bash
keytool -genkey -v -keystore ~/kotoba-upload.jks -keyalg RSA -keysize 2048 -validity 10000 -alias upload
cat > src-tauri/gen/android/keystore.properties <<EOF
password=<your keystore password>
keyAlias=upload
storeFile=/Users/<you>/kotoba-upload.jks
EOF
```

`keystore.properties` and `*.jks` are git-ignored – keep a backup of the keystore, you need the same
key for every update. For CI add the secrets `ANDROID_KEYSTORE_BASE64` (`base64 -i kotoba-upload.jks`),
`ANDROID_KEYSTORE_PASSWORD`, `ANDROID_KEY_ALIAS`.

Google Play: create the app in the Play Console, upload the `.aab` to *Internal testing* first,
data safety form: *no data collected*. The version code comes from `bundle.android.versionCode` in
`src-tauri/tauri.conf.json` – increase it for every upload.

## 6. Icons, fonts, world

```bash
make icons     # regenerate web + desktop + iOS icons from the 言 stamp (tools/icons.py)
make fonts     # re-subset fonts after adding new kanji/kana to src/index.html
make world     # regenerate the RPG map and embed it into src/index.html
```

## 7. Versioning

The version lives in **`package.json`** (Tauri reads it from there). Bump it, update
`CHANGELOG.md`, then tag – see [RELEASING.md](RELEASING.md).

## Troubleshooting

| Problem | Fix |
|---|---|
| `failed to run custom build command for tauri` (Linux) | install the apt packages above |
| `xcrun: error: SDK "iphoneos" cannot be located` | `sudo xcode-select -s /Applications/Xcode.app` |
| iOS: “No signing certificate” | choose a Team in Xcode or set `APPLE_DEVELOPMENT_TEAM` |
| Android: `NDK_HOME` / `JAVA_HOME` not set | see the exports in section 5, open a new terminal |
| App shows an old version | `make build` runs automatically before `tauri build`; delete `src-tauri/target` if in doubt |
| No sound before the first tap | system rule on iOS/browsers – Kotoba starts audio after the first interaction |
