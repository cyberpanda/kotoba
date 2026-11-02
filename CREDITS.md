# Credits, Sources & Licenses

Kotoba is an open-source project (MIT, see [LICENSE](LICENSE)) by **CyberPanda**
([GitHub](https://github.com/CyberPanda) · [X @realcyberpanda](https://x.com/realcyberpanda)).

## Good-faith notice

This project was developed entirely with AI. The AI was instructed to use **only open-source,
public-domain or self-created content** for anything external, and to never copy copyrighted
material (lyrics, artwork, sprites, characters, logos). Everything was done to the best of
our knowledge and in good faith.

If you believe any part of this project infringes your rights, please open an issue on GitHub or
contact [@realcyberpanda](https://x.com/realcyberpanda) – it will be credited correctly or removed promptly.

## Created for this project (MIT)

- All code (HTML, CSS, JavaScript)
- All illustrations and icons (SVG drawn in code): Mt. Fuji banner, Japan scenes, picture-path
  images, app icon (言 stamp), falling leaves
- All pixel art (drawn in code): RPG characters, tiles, items, the lucky cat in Maneki Run
- All music and sound effects: generated live in the browser with the Web Audio API, including the per-region adventure themes and ambiences (birdsong, station chime, city hum, waves, cicadas, temple bell, crowd, wind) – all original, no samples
  (Sakura Piano, Lofi Yoru, Koto Ame, Ame no Mado, Shakuhachi Kaze, Zen Niwa, Matsuri,
  City Pop Yoru, Pixel Tabi, Neko Dash, Kumo) – no audio files are included
- All vocabulary lists, example sentences, translations, mnemonics, grammar notes,
  anime-phrase explanations, RPG quests and dialogue
- Song lyrics “風の歌 / Song of the Wind” and “星の約束 / Promise of Stars”

## Third-party code (loaded on demand)

- [three.js](https://github.com/mrdoob/three.js) r128 – © 2010–2021 three.js authors, MIT License. Loaded from cdnjs only when 3D β is switched on.
- three.js examples (EffectComposer, RenderPass, ShaderPass, UnrealBloomPass, CopyShader, LuminosityHighPassShader) – same MIT License, loaded from jsDelivr only when 🧪 experimental graphics are on in 3D.
- three.js examples SSAOPass, SSAOShader and SimplexNoise – MIT License, loaded from jsDelivr only when ✨ shader mods are on.
- [piper-plus](https://github.com/ayutaz/piper-plus) 0.6.0 – MIT License; Japanese neural text-to-speech, loaded from jsDelivr only when an HQ voice is chosen. Uses [ONNX Runtime Web](https://github.com/microsoft/onnxruntime) (MIT) and OpenJTalk-based Japanese text processing.
- HQ voice “Tsukuyomi-chan” – piper-plus model by ayousanz (Hugging Face), trained on the **つくよみちゃんコーパス (CV.夢前黎)** © Rei Yumesaki; used under the Tsukuyomi-chan corpus terms, which require this credit. Downloaded by the user’s browser on demand, not bundled.
- HQ voice “CSS10 Japanese” – piper-plus model by ayousanz, trained on the CSS10 Japanese dataset (based on public-domain LibriVox recordings). Downloaded on demand, not bundled.
- Model licenses were not stated on the model pages at the time of writing; please check the Hugging Face model cards. If a rights holder objects, the voice will be removed.
- All 3D models and textures are generated procedurally in code for this project (MIT); no external models are used.

- Kotoba Voice – self-made formant speech synthesizer (Web Audio API), MIT

## Native app shell & build tools

- [Tauri 2](https://github.com/tauri-apps/tauri) – MIT / Apache-2.0; wraps the web app for iOS, Android, macOS, Windows and Linux (not part of the web version).
- Build and test tools (not shipped): [Playwright](https://github.com/microsoft/playwright) (Apache-2.0), [Pillow](https://github.com/python-pillow/Pillow) (MIT-CMU), [fontTools](https://github.com/fonttools/fonttools) (MIT).

## Third-party content

| What | Author / Owner | License | How it is used |
|---|---|---|---|
| Noto Sans CJK JP → bundled subset “Kotoba Sans” | © 2014-2021 Adobe, Google (Noto project) | SIL Open Font License 1.1 – [src/fonts/OFL.txt](src/fonts/OFL.txt) | Bundled in `src/fonts/`, embedded in the standalone file |
| Noto Serif CJK JP → bundled subset “Kotoba Serif” | © 2017-2023 Adobe, Google (Noto project) | SIL Open Font License 1.1 – [src/fonts/OFL.txt](src/fonts/OFL.txt) | Bundled in `src/fonts/`, embedded in the standalone file |
| DejaVu Sans Mono → bundled subset “Kotoba Mono” | © 2003 Bitstream, Inc.; DejaVu changes public domain | Bitstream Vera license – [src/fonts/LICENSE-DejaVu.txt](src/fonts/LICENSE-DejaVu.txt) | Bundled in `src/fonts/`, embedded in the standalone file |
| Haiku 古池や… and 閑さや… | Matsuo Bashō (1644–1694) | Public domain | Original Japanese text; translations by this project |
| Haiku 雪とけて… | Kobayashi Issa (1763–1828) | Public domain | Original Japanese text; translation by this project |
| Haiku 柿食えば… | Masaoka Shiki (1867–1902) | Public domain | Original Japanese text; translation by this project |
| Seigaiha wave pattern | Traditional Japanese motif | Public domain | Redrawn in code |
| Text-to-speech voices | Your operating system / browser vendor | Their own terms | Used live via the browser’s Web Speech API; no audio is shipped |

No sprites, images, sounds or texts were downloaded from other sources. The fonts are bundled, so the app makes no requests to Google Fonts or any other third party.

## Mentioned but not included

- **Ninja Adventure Asset Pack** by pixel-boy – CC0 1.0 – <https://pixel-boy.itch.io/ninja-adventure-asset-pack>.
  Recommended as an optional future sprite set. Not part of this repository yet; if added, it will be listed above.
- *Ragnarok Online*, *Game Boy*, *Subway Surfers* and other product names are trademarks of their
  respective owners. They were mentioned only as style inspiration; no assets of them are used.
