#!/usr/bin/env python3
"""Generate every app icon from the 言 stamp mark.

Writes:
  src/icons/              web / PWA icons (favicon, apple-touch, 192/512, maskable, 1024 master)
  src-tauri/icons/        desktop (icns, ico, png) + ios/AppIcon-*.png
Needs: pip install pillow playwright && python3 -m playwright install chromium
"""
import os, io
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, "src", "icons")
APP = os.path.join(ROOT, "src-tauri", "icons")
MARK = open(os.path.join(WEB, "mark.svg-fragment"), encoding="utf-8").read()
BG = "#0c1222"
WAVES = '<path d="M0 400q64-36 128 0t128 0 128 0 128 0V512H0z" fill="#18264a"/><path d="M0 440q64-30 128 0t128 0 128 0 128 0V512H0z" fill="#22335e"/>'


def svg(rx, scale, tx, ty, waves=True):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" rx="{rx}" fill="{BG}"/>'
            f'{WAVES if waves else ""}<g transform="translate({tx} {ty}) scale({scale})">{MARK}</g></svg>')


V = {"rounded": svg(112, 3.2, 96, 76), "square": svg(0, 3.2, 96, 76), "maskable": svg(0, 2.5, 131, 116), "favicon": svg(96, 4.6, 26, 26, False)}


def render(pg, s, n):
    s = s.replace("<svg ", f'<svg width="{n}" height="{n}" ', 1)
    pg.set_viewport_size({"width": n, "height": n})
    pg.set_content(f'<body style="margin:0;background:transparent">{s}</body>')
    return Image.open(io.BytesIO(pg.screenshot(omit_background=True))).convert("RGBA")


def main():
    os.makedirs(os.path.join(APP, "ios"), exist_ok=True)
    with sync_playwright() as p:
        pg = p.chromium.launch().new_page()
        sq = render(pg, V["square"], 1024).convert("RGB")
        rd = render(pg, V["rounded"], 1024)
        mk = render(pg, V["maskable"], 512).convert("RGB")
        fv = render(pg, V["favicon"], 256)
    # web
    for name, s in [("icon.svg", V["rounded"]), ("icon-maskable.svg", V["maskable"]), ("favicon.svg", V["favicon"])]:
        open(os.path.join(WEB, name), "w").write(s)
    sq.save(os.path.join(WEB, "kotoba-icon-1024.png"))
    sq.resize((180, 180), Image.LANCZOS).save(os.path.join(WEB, "kotoba-icon-180.png"))
    for n in (192, 512):
        rd.resize((n, n), Image.LANCZOS).save(os.path.join(WEB, f"kotoba-icon-{n}.png"))
        mk.resize((n, n), Image.LANCZOS).save(os.path.join(WEB, f"kotoba-icon-maskable-{n}.png"))
    fv.resize((32, 32), Image.LANCZOS).save(os.path.join(WEB, "favicon-32.png"))
    fv.save(os.path.join(WEB, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    # macOS: Apple grid – 824px artwork centred on a 1024 canvas
    mac = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
    mac.paste(rd.resize((824, 824), Image.LANCZOS), (100, 100))
    mac.save(os.path.join(APP, "icon.icns"))
    mac.save(os.path.join(APP, "icon.png"))
    for n, f in [(32, "32x32.png"), (128, "128x128.png"), (256, "128x128@2x.png"), (64, "64x64.png")]:
        rd.resize((n, n), Image.LANCZOS).save(os.path.join(APP, f))
    rd.save(os.path.join(APP, "icon.ico"), sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    for n in (30, 44, 71, 89, 107, 142, 150, 284, 310):
        rd.resize((n, n), Image.LANCZOS).save(os.path.join(APP, f"Square{n}x{n}Logo.png"))
    rd.resize((50, 50), Image.LANCZOS).save(os.path.join(APP, "StoreLogo.png"))
    # iOS / iPadOS (opaque, full-bleed – iOS applies the mask)
    for base, scales in [(20, ["1x", "2x", "2x-1", "3x"]), (29, ["1x", "2x", "2x-1", "3x"]), (40, ["1x", "2x", "2x-1", "3x"]),
                         (60, ["2x", "3x"]), (76, ["1x", "2x"]), (83.5, ["2x"]), (512, ["2x"])]:
        for sc in scales:
            px = round(base * int(sc[0]))
            b = int(base) if base != 83.5 else base
            sq.resize((px, px), Image.LANCZOS).save(os.path.join(APP, "ios", f"AppIcon-{b}x{b}@{sc}.png"))
    # Android launcher icons (legacy square/round + adaptive foreground with 66% safe zone)
    for dpi, n in [("mdpi", 48), ("hdpi", 72), ("xhdpi", 96), ("xxhdpi", 144), ("xxxhdpi", 192)]:
        d = os.path.join(APP, "android", f"mipmap-{dpi}")
        os.makedirs(d, exist_ok=True)
        rd.resize((n, n), Image.LANCZOS).save(os.path.join(d, "ic_launcher.png"))
        circ = Image.new("L", (n * 4, n * 4), 0)
        from PIL import ImageDraw
        ImageDraw.Draw(circ).ellipse((0, 0, n * 4, n * 4), fill=255)
        r = sq.resize((n, n), Image.LANCZOS).convert("RGBA")
        r.putalpha(circ.resize((n, n), Image.LANCZOS))
        r.save(os.path.join(d, "ic_launcher_round.png"))
        fg = int(n * 108 / 48)
        mk.resize((fg, fg), Image.LANCZOS).save(os.path.join(d, "ic_launcher_foreground.png"))
    print("icons written to", WEB, "and", APP)


if __name__ == "__main__":
    main()
