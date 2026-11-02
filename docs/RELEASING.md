# Releasing

1. Update `version` in `package.json` (semver, e.g. `2.1.0`), raise `bundle.android.versionCode` in `src-tauri/tauri.conf.json`, and add a section to `CHANGELOG.md`.
2. `make build && make qa` – the QA run must print `QA passed`.
3. Commit, then tag and push:

```bash
git commit -am "Release v2.1.0"
git tag v2.1.0
git push && git push --tags
```

4. GitHub Actions → **Release** creates a *draft* release with:

| File | Platform |
|---|---|
| `kotoba-web-2.1.0.zip` | split site for any web server |
| `kotoba-standalone-2.1.0.zip` | one-file version + extras |
| `Kotoba_2.1.0_universal.dmg` | macOS (Apple Silicon + Intel) |
| `Kotoba_2.1.0_x64-setup.exe`, `.msi`, `Kotoba_2.1.0_arm64-setup.exe` | Windows x64 / ARM64 |
| `Kotoba_2.1.0_amd64.AppImage`, `_aarch64.AppImage`, `.deb`, `.rpm` | Linux x64 / ARM64 |
| `Kotoba_2.1.0_android.apk`, `.aab` | Android (signed if the keystore secrets are set) |
| `Kotoba.ipa` | iOS/iPadOS (only if enabled, see below) |

5. Optionally attach locally built files (e.g. the signed `.dmg` / `.ipa` from your Mac), review the
   notes, **Publish**.

## Secrets (Settings → Secrets and variables → Actions)

| Name | Needed for |
|---|---|
| `APPLE_CERTIFICATE`, `APPLE_CERTIFICATE_PASSWORD`, `APPLE_SIGNING_IDENTITY`, `APPLE_ID`, `APPLE_PASSWORD`, `APPLE_TEAM_ID` | signed + notarized macOS build (optional) |
| `APPLE_API_ISSUER`, `APPLE_API_KEY_ID`, `APPLE_API_KEY_P8` (content of the .p8) | iOS build in CI |
| `ANDROID_KEYSTORE_BASE64`, `ANDROID_KEYSTORE_PASSWORD`, `ANDROID_KEY_ALIAS` | signed Android build |
| `PAGES_DEPLOY_TOKEN` | updates `kotoba.html` + extras in the live-demo repo (`cyberpanda.github.io`, change with variable `PAGES_REPO`). Fine-grained token, *Contents: read and write* on that repo only |
| variable `IOS_RELEASE` = `true` | enables the iOS job (requires committed `src-tauri/gen/apple`) |

Without secrets the workflow still produces unsigned macOS/Windows/Linux builds.

## Web deployment

The **live demo** (`https://cyberpanda.github.io/kotoba.html`) is updated by the `live-demo` job on every release tag when `PAGES_DEPLOY_TOKEN` is set.

Every push to `main` deploys `dist/web` to GitHub Pages (`pages.yml`). For your own server use the
web zip from the release – see [DEPLOY-WEB.md](DEPLOY-WEB.md).
