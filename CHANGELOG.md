# Changelog

## 2.0.0 – 2026-10-29

- Professional repository layout: `src/` (app), `src-tauri/` (native shell), `tools/`, `deploy/`, `docs/`
- Native apps via Tauri 2: macOS universal, iOS/iPadOS (.ipa), Android (.apk/.aab), Windows (.exe/.msi), Linux (.AppImage/.deb/.rpm)
- Split web build (`dist/web`) with hashed assets, service worker, manifest, `.htaccess`; one-file build kept (`dist/standalone`)
- Deployment configs for nginx, Apache, Caddy, Docker; GitHub Actions for CI (build + browser QA), releases and Pages
- New 言 stamp identity (indigo & vermilion), animated splash with sound, guided tour, calm default music

## 1.0.0 – Initial release

### Learning
- Vocabulary with kana, kanji, romaji, meanings, mnemonics and example sentences
- Spaced repetition (SM-2) sessions, topic and word selection, saved and hard words
- Learning path (JLPT N5): 8 stages with dialogues, comprehension questions, tests and a placement test
- Grammar, kana and kanji modes, “When what?” guide, reading texts and haiku
- Build mode: arrange sentences from word tiles, typing and free writing

### Games & chill modes
- Picture path, challenge, give & take, こそあど, kanji in sentences, song gaps, phrase quiz, pronouns
- Bōken RPG: 12 chapter worlds across Japan connected by train, 34 maps plus 19 enterable buildings with scrolling camera, landmark pixel art, passing trains, station menu with animated train rides, 🧭 goal guide, main/side quest markers, 47 quests, adaptive full-width view, floating joystick, city traffic and pedestrians with mini vocabulary quests, signposted exits, tracks at every station, rideable subway between Tokyo districts, sharp high-DPI rendering, optional 2.5D view (tilted ground with upright sprites and side-view trains), 8-way movement, Shibuya scramble crossing, rounded curbs and shores, travel guide book, gradually increasing Japanese, bag, hints and on-screen gamepad; a synthesized theme and ambience per region (birds, station chime, city, waves, cicadas, temple bell, crowd, wind)
- Maneki Run endless runner with lanes, the lucky cat seen from behind, staggered word cards, a slight tilt, stackable sprint, combos and levels
- Bonsai, zen garden, koi pond with unlockable decor, breathing exercise

### Experience
- 33 labeled Japan scenes with read-aloud on the home screen
- Read-aloud via system voices or the built-in offline Kotoba Voice; correct particle pronunciation
- Procedurally generated music and sound effects, each switchable
- Settings menu: music, sounds, read-aloud, optional translation blur, display
- Dark and light theme, English and German interface
- Responsive layout for phones, tablets and desktops in portrait and landscape; mouse drag and arrows for carousels

### Platform
- Single self-contained HTML file, installable PWA, works offline
- All fonts bundled locally; no tracking, no cookies, no third-party requests
- GitHub Pages build (`site/`) and Linux installer (`linux/`)
