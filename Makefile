# Kotoba – common tasks. `make help` lists them.
PY ?= python3
VERSION := $(shell $(PY) -c "import json;print(json.load(open('package.json'))['version'])")

.PHONY: help build serve qa icons fonts world app mac ios-init ios-dev ipa ipa-adhoc android-init android-dev apk aab release-zips docker clean

help:            ## show this help
	@grep -E '^[a-z-]+:.*##' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  %-14s %s\n",$$1,$$2}'

build:           ## build dist/web, dist/standalone, dist/embed
	$(PY) tools/build.py

serve: build     ## serve dist/web on http://localhost:8080
	$(PY) -m http.server 8080 --directory dist/web

qa: build        ## automated browser QA (needs requirements-dev.txt + playwright chromium)
	$(PY) tools/qa.py

icons:           ## regenerate all icons from the 言 stamp
	$(PY) tools/icons.py

fonts:           ## re-subset bundled fonts (after adding new characters)
	$(PY) tools/build_fonts.py

world:           ## regenerate RPG world and embed it into src/index.html
	$(PY) tools/world/gen_world.py

node_modules: package.json
	npm install

app: node_modules  ## desktop app for this machine (macOS .app/.dmg, Windows .exe/.msi, Linux .AppImage/.deb)
	npx tauri build

mac: node_modules  ## macOS universal (Apple Silicon + Intel) .app + .dmg
	rustup target add aarch64-apple-darwin x86_64-apple-darwin
	npx tauri build --target universal-apple-darwin

ios-init: node_modules  ## create the Xcode project (once, on macOS)
	rustup target add aarch64-apple-ios aarch64-apple-ios-sim x86_64-apple-ios
	npx tauri ios init
	$(PY) tools/ios_setup.py

ios-dev: node_modules   ## run on simulator / connected iPhone or iPad
	npx tauri ios dev

ipa: node_modules       ## build a signed .ipa for App Store / TestFlight
	npx tauri ios build --export-method app-store-connect

ipa-adhoc: node_modules ## build a .ipa for registered test devices
	npx tauri ios build --export-method release-testing

android-init: node_modules  ## once: create the Android Studio project
	rustup target add aarch64-linux-android armv7-linux-androideabi i686-linux-android x86_64-linux-android
	npx tauri android init
	$(PY) tools/android_setup.py

android-dev: node_modules   ## run on emulator / connected Android device
	npx tauri android dev

apk: node_modules           ## universal .apk (sideload / F-Droid / direct download)
	npx tauri android build --apk

aab: node_modules           ## .aab for Google Play
	npx tauri android build --aab

release-zips: build     ## zips for manual hosting
	cd dist/web && zip -qr ../kotoba-web-$(VERSION).zip .
	cd dist/standalone && zip -qr ../kotoba-standalone-$(VERSION).zip .

docker:          ## build and run the nginx image on :8080
	docker compose up --build

clean:
	rm -rf dist src-tauri/target
