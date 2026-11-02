#!/usr/bin/env python3
"""Kotoba build.

Reads src/index.html and produces:

  dist/web/          split static site (index.html + assets/ + fonts/ + icons/ + sw.js)
  dist/standalone/   kotoba.html – everything in one file (+ optional PWA extras)
  dist/embed/        kotoba-embed.html – single file without head/PWA tags (for sandboxed hosts)

Usage:  python3 tools/build.py [--out dist]
"""
import base64, hashlib, json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
OUT = os.path.join(ROOT, sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "dist")

PKG = json.load(open(os.path.join(ROOT, "package.json"), encoding="utf-8"))
VERSION = PKG["version"]
HTML = open(os.path.join(SRC, "index.html"), encoding="utf-8").read()
KVER = re.search(r'const KVER="(\d+)"', HTML).group(1)
THEME = "#0c1222"

FONTS = [("Kotoba Sans", 400, "KotobaSans-Regular.woff"), ("Kotoba Sans", 700, "KotobaSans-Bold.woff"),
         ("Kotoba Serif", 700, "KotobaSerif-Bold.woff"), ("Kotoba Mono", 400, "KotobaMono-Regular.woff")]
FONT_DIR = os.path.join(SRC, "fonts")
ICON_DIR = os.path.join(SRC, "icons")


def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()


def font_css(prefix=None):
    o = ""
    for fam, w, f in FONTS:
        u = prefix + f if prefix is not None else b64(os.path.join(FONT_DIR, f), "font/woff")
        o += f'@font-face{{font-family:"{fam}";font-weight:{w};font-style:normal;font-display:swap;src:url("{u}") format("woff")}}'
        if w == 700 and fam == "Kotoba Sans":
            o += f'@font-face{{font-family:"{fam}";font-weight:600 900;font-style:normal;font-display:swap;src:url("{u}") format("woff")}}'
    return o


def write(path, data, mode="w"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if mode == "w":
        open(path, "w", encoding="utf-8").write(data)
    else:
        open(path, "wb").write(data)


def manifest(start, icons_prefix, maskable=True):
    icons = [{"src": f"{icons_prefix}kotoba-icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
             {"src": f"{icons_prefix}kotoba-icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"}]
    if maskable:
        icons += [{"src": f"{icons_prefix}kotoba-icon-maskable-192.png", "sizes": "192x192", "type": "image/png", "purpose": "maskable"},
                  {"src": f"{icons_prefix}kotoba-icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]
    return json.dumps({
        "name": "Kotoba – Learn Japanese", "short_name": "Kotoba", "id": start, "start_url": start, "scope": "./",
        "display": "standalone", "display_override": ["standalone", "fullscreen"], "orientation": "any",
        "background_color": THEME, "theme_color": THEME, "lang": "en", "categories": ["education"],
        "description": "Learn Japanese interactively – lessons, learning path, games, RPG and chill modes. Works offline.",
        "icons": icons}, ensure_ascii=False, indent=1)


HEAD_META = f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="Kotoba – learn Japanese interactively: vocabulary, reading, sentence building, games, spaced repetition. English or German.">
<meta name="theme-color" content="{THEME}">
<meta name="color-scheme" content="dark light">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Kotoba">
<meta name="generator" content="Kotoba {VERSION} (build {KVER})">
'''
BASE_CSS = "*{box-sizing:border-box}:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;-webkit-text-size-adjust:100%;text-size-adjust:100%}[hidden]{display:none!important}"

# ---- split source -------------------------------------------------------------------------
body = HTML.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
body = re.sub(r'^<meta charset="utf-8">\n', "", body)
title = re.search(r"<title>.*?</title>\n?", body).group(0)
body = body.replace(title, "", 1)
src_icon_links = re.findall(r'<link rel="(?:icon|apple-touch-icon)" href="data:[^"]*">\n?', body)
for l in src_icon_links:
    body = body.replace(l, "", 1)

styles = []
def grab_style(m):
    styles.append(m.group(1))
    return ""
body_nostyle = re.sub(r"<style[^>]*>(.*?)</style>\n?", grab_style, body, flags=re.S)
scripts = []
def grab_script(m):
    scripts.append(m.group(1))
    return f"<!--SCRIPT{len(scripts)-1}-->"
markup = re.sub(r"<script>(.*?)</script>", grab_script, body_nostyle, flags=re.S)
assert len(scripts) == 2, f"expected 2 inline scripts, found {len(scripts)}"
SCRIPT_NAMES = ["splash", "app"]

ICONS = sorted(os.listdir(ICON_DIR))


def page(head_extra, html_body, lang_title=title):
    return "<!doctype html>\n<html lang=\"en\">\n<head>\n" + HEAD_META + lang_title + head_extra + "</head>\n<body>\n" + html_body.strip() + "\n</body>\n</html>\n"


# ---- dist/web (split) -----------------------------------------------------------------------
def build_web():
    d = os.path.join(OUT, "web")
    shutil.rmtree(d, ignore_errors=True)
    css = BASE_CSS + "\n" + "\n".join(s.replace("/*FONTS*/", "") for s in styles)
    css_name = f"kotoba.{hashlib.sha1(css.encode()).hexdigest()[:8]}.css"
    write(os.path.join(d, "assets", css_name), css)
    write(os.path.join(d, "assets", "fonts.css"), font_css("../fonts/"))
    js_files = []
    for i, code in enumerate(scripts):
        n = f"{SCRIPT_NAMES[i]}.{hashlib.sha1(code.encode()).hexdigest()[:8]}.js"
        write(os.path.join(d, "assets", n), code)
        js_files.append(n)
    shutil.copytree(FONT_DIR, os.path.join(d, "fonts"))
    os.makedirs(os.path.join(d, "icons"), exist_ok=True)
    for f in ICONS:
        shutil.copy(os.path.join(ICON_DIR, f), os.path.join(d, "icons", f))
    shutil.copy(os.path.join(ICON_DIR, "favicon.ico"), os.path.join(d, "favicon.ico"))
    write(os.path.join(d, "manifest.webmanifest"), manifest("./", "icons/"))
    head = (f'<link rel="icon" href="favicon.ico" sizes="48x48">\n<link rel="icon" href="icons/favicon.svg" type="image/svg+xml">\n'
            f'<link rel="apple-touch-icon" href="icons/kotoba-icon-180.png">\n<link rel="manifest" href="manifest.webmanifest">\n'
            f'<link rel="preload" href="fonts/KotobaSans-Regular.woff" as="font" type="font/woff" crossorigin>\n'
            f'<link rel="stylesheet" href="assets/fonts.css">\n<link rel="stylesheet" href="assets/{css_name}">\n')
    html = markup
    for i, n in enumerate(js_files):
        html = html.replace(f"<!--SCRIPT{i}-->", f'<script src="assets/{n}"></script>')
    html += '\n<script>if("serviceWorker"in navigator&&location.protocol.startsWith("http"))addEventListener("load",()=>navigator.serviceWorker.register("sw.js").catch(()=>{}))</script>'
    write(os.path.join(d, "index.html"), page(head, html))
    files = ["./", "index.html", "manifest.webmanifest", "favicon.ico", "assets/fonts.css", f"assets/{css_name}"] + \
            [f"assets/{n}" for n in js_files] + [f"fonts/{f}" for f in os.listdir(FONT_DIR) if f.endswith(".woff")] + [f"icons/{f}" for f in ICONS]
    write(os.path.join(d, "sw.js"), SW_TEMPLATE.replace("__CACHE__", f"kotoba-web-{KVER}").replace("__FILES__", json.dumps(files)))
    write(os.path.join(d, "version.json"), json.dumps({"version": VERSION, "build": int(KVER)}))
    write(os.path.join(d, "robots.txt"), "User-agent: *\nAllow: /\n")
    ht = os.path.join(ROOT, "deploy", "apache.htaccess")
    if os.path.exists(ht):
        shutil.copy(ht, os.path.join(d, ".htaccess"))
    return d


SW_TEMPLATE = '''/* Kotoba service worker – generated by tools/build.py */
const CACHE="__CACHE__",FILES=__FILES__;
self.addEventListener("install",e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(FILES)));self.skipWaiting()});
self.addEventListener("activate",e=>e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x.startsWith("kotoba-web-")&&x!==CACHE).map(x=>caches.delete(x)))).then(()=>self.clients.claim())));
self.addEventListener("fetch",e=>{const r=e.request;if(r.method!=="GET")return;const u=new URL(r.url);
 if(u.origin!==location.origin){e.respondWith(caches.match(r).then(h=>h||fetch(r).then(x=>{if(x.ok||x.type==="opaque"){const c=x.clone();caches.open("kotoba-res").then(y=>y.put(r,c))}return x})));return}
 e.respondWith(fetch(r).then(x=>{if(x.ok){const c=x.clone();caches.open(CACHE).then(y=>y.put(r,c))}return x}).catch(()=>caches.match(r,{ignoreSearch:true}).then(h=>h||caches.match("index.html"))))});
'''

STANDALONE_SW = '''const C="kotoba-standalone-__V__",F=["kotoba.html"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(F)));self.skipWaiting()});
self.addEventListener("activate",e=>e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x.startsWith("kotoba-standalone")&&x!==C).map(x=>caches.delete(x)))).then(()=>self.clients.claim())));
self.addEventListener("fetch",e=>{const u=new URL(e.request.url);if(e.request.method!=="GET"||u.origin!==location.origin||!/\\/kotoba[^/]*$/.test(u.pathname))return;e.respondWith(fetch(e.request).then(r=>{const c=r.clone();caches.open(C).then(x=>x.put(e.request,c));return r}).catch(()=>caches.match(e.request,{ignoreSearch:true})))});
'''


def inline_html(head_extra, extra_body=""):
    html = markup
    for i, code in enumerate(scripts):
        html = html.replace(f"<!--SCRIPT{i}-->", "<script>" + code + "</script>")
    css = BASE_CSS + font_css() + "\n" + "\n".join(s.replace("/*FONTS*/", "") for s in styles)
    return page(head_extra + "<style>" + css + "</style>\n", html + extra_body)


# ---- dist/standalone (single file) -----------------------------------------------------------
def build_standalone():
    d = os.path.join(OUT, "standalone")
    shutil.rmtree(d, ignore_errors=True)
    I = {k: b64(os.path.join(ICON_DIR, f), "image/png") for k, f in
         [("f32", "favicon-32.png"), ("a180", "kotoba-icon-180.png"), ("i192", "kotoba-icon-192.png"),
          ("i512", "kotoba-icon-512.png"), ("m512", "kotoba-icon-maskable-512.png")]}
    mk = ('<script>(()=>{const I=%s;const L=document.createElement("link");L.rel="manifest";'
          'const ios=/iPhone|iPad|iPod/.test(navigator.userAgent)||(navigator.platform==="MacIntel"&&navigator.maxTouchPoints>1);'
          'const mk=()=>{if(ios)return;const u=location.href.split("#")[0],m={name:"Kotoba – Learn Japanese",short_name:"Kotoba",id:u,start_url:u,'
          'scope:u.replace(/[^/]*$/,""),display:"standalone",orientation:"any",background_color:"%s",theme_color:"%s",'
          'icons:[{src:I.i192,sizes:"192x192",type:"image/png",purpose:"any"},{src:I.i512,sizes:"512x512",type:"image/png",purpose:"any"},{src:I.m512,sizes:"512x512",type:"image/png",purpose:"maskable"}]};'
          'L.href=URL.createObjectURL(new Blob([JSON.stringify(m)],{type:"application/manifest+json"}));document.head.appendChild(L)};'
          'if(location.protocol==="file:")mk();else fetch("kotoba.webmanifest",{method:"HEAD"}).then(r=>{if(r.ok){L.href="kotoba.webmanifest";document.head.appendChild(L)}else mk()}).catch(mk)})()</script>\n'
          ) % (json.dumps({k: I[k] for k in ("i192", "i512", "m512")}), THEME, THEME)
    head = (f'<link rel="icon" href="{b64(os.path.join(ICON_DIR, "favicon.svg"), "image/svg+xml")}" type="image/svg+xml">\n'
            f'<link rel="icon" href="{I["f32"]}" sizes="32x32" type="image/png">\n<link rel="apple-touch-icon" href="{I["a180"]}">\n' + mk)
    sw = '\n<script>if("serviceWorker"in navigator&&location.protocol.startsWith("http"))addEventListener("load",()=>fetch("kotoba-sw.js",{method:"HEAD"}).then(r=>{if(r.ok)navigator.serviceWorker.register("kotoba-sw.js",{scope:"./kotoba"})}).catch(()=>{}))</script>'
    write(os.path.join(d, "kotoba.html"), inline_html(head, sw))
    ex = os.path.join(d, "extras")
    write(os.path.join(ex, "kotoba-sw.js"), STANDALONE_SW.replace("__V__", KVER))
    m = json.loads(manifest("./kotoba.html", ""))
    m["scope"] = "./"
    write(os.path.join(ex, "kotoba.webmanifest"), json.dumps(m, ensure_ascii=False, indent=1))
    for f in ["favicon.ico", "kotoba-icon-180.png", "kotoba-icon-192.png", "kotoba-icon-512.png",
              "kotoba-icon-maskable-192.png", "kotoba-icon-maskable-512.png"]:
        shutil.copy(os.path.join(ICON_DIR, f), os.path.join(ex, f))
    return d


# ---- dist/embed (single file for sandboxed hosts, no PWA tags) -------------------------------
def build_embed():
    d = os.path.join(OUT, "embed")
    shutil.rmtree(d, ignore_errors=True)
    pub = HTML.replace("/*FONTS*/", font_css())
    write(os.path.join(d, "kotoba-embed.html"), pub)
    return d


if __name__ == "__main__":
    for fn in (build_web, build_standalone, build_embed):
        p = fn()
        size = sum(os.path.getsize(os.path.join(a, f)) for a, _, fs in os.walk(p) for f in fs)
        print(f"{os.path.relpath(p, ROOT):18} {size/1024:8.0f} KB")
    print(f"Kotoba {VERSION} (build {KVER}) -> {os.path.relpath(OUT, ROOT)}/")
