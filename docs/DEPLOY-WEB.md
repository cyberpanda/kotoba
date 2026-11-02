# Hosting Kotoba on your own web server

Kotoba is a static web app – no database, no backend, no build step on the server.
There are two flavours; both are produced by:

```bash
python3 tools/build.py        # or: make build
```

| | `dist/web/` – **split site** | `dist/standalone/kotoba.html` – **one file** |
|---|---|---|
| Files | `index.html`, `assets/*.css|js` (hashed), `fonts/`, `icons/`, `sw.js`, `manifest.webmanifest`, `.htaccess` | one 3 MB HTML file (+ optional `extras/`) |
| Caching | assets cached for a year, only `index.html`/`sw.js` revalidate → fast updates | whole file re-downloaded on change |
| Offline / install | full PWA (service worker + manifest) | works offline from `file://`; for PWA on a server copy `extras/*` next to it |
| Best for | a domain or sub-folder you control | dropping into an existing site, USB stick, e-mail |

Both run under any path (`/`, `/kotoba/`, `/apps/kotoba/…`) – all URLs are relative.

> **HTTPS is required** for the service worker, “Install app” and audio on iOS. Plain `http://`
> works only on `localhost`.

---

## 1. Quick start

```bash
make serve                       # http://localhost:8080 (python http.server)
docker compose up --build        # http://localhost:8080 (nginx, production-like)
```

## 2. Any web host (FTP / shared hosting)

1. `python3 tools/build.py`
2. Upload the **contents** of `dist/web/` into a folder, e.g. `public_html/kotoba/`
   (Apache picks up the included `.htaccess` automatically).
3. Open `https://your-domain/kotoba/`.

**Update:** upload the new `dist/web/` again (overwrite). Old hashed assets may be deleted.
Users get the update on their next visit – progress is kept (it lives in the browser’s storage).

## 3. nginx

```bash
sudo mkdir -p /var/www/kotoba && sudo rsync -a --delete dist/web/ /var/www/kotoba/
sudo cp deploy/nginx.conf /etc/nginx/sites-available/kotoba
sudo ln -s /etc/nginx/sites-available/kotoba /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

Sub-folder instead of own server block:

```nginx
location /kotoba/ {
    alias /var/www/kotoba/;
    try_files $uri $uri/ /kotoba/index.html;
}
```

HTTPS: `sudo certbot --nginx -d kotoba.example.com`.

## 4. Apache

Copy `dist/web/` into the document root (or a sub-folder). The `.htaccess` sets MIME types,
compression and cache headers. Needs `AllowOverride All` (or copy `deploy/apache.htaccess` into
your vhost) and the modules `headers` + `deflate` (`a2enmod headers deflate`).

## 5. Caddy (automatic HTTPS)

```bash
sudo rsync -a --delete dist/web/ /srv/kotoba/
sudo cp deploy/Caddyfile /etc/caddy/Caddyfile   # change the domain inside
sudo systemctl reload caddy
```

## 6. Docker

```bash
docker build -t kotoba .
docker run -d --name kotoba -p 8080:80 --restart unless-stopped kotoba
```

Put it behind your reverse proxy (Traefik, nginx proxy manager, Caddy) for HTTPS.

## 7. GitHub Pages / Netlify / Cloudflare Pages / Vercel

* **GitHub Pages:** the included workflow `.github/workflows/pages.yml` builds and deploys on every
  push to `main` (Settings → Pages → Source: *GitHub Actions*).
* **Netlify / Cloudflare Pages / Vercel:** build command `python3 tools/build.py`, output directory
  `dist/web`.

## 8. One-file version on a server

Upload `dist/standalone/kotoba.html`. Icons for browser tab and iPhone home screen are embedded.
For Android “Install app” and offline caching also upload the files from
`dist/standalone/extras/` into the **same folder**:

```
kotoba.html  kotoba.webmanifest  kotoba-sw.js  favicon.ico  kotoba-icon-*.png
```

Without the extras the 404s for `kotoba.webmanifest` / `kotoba-sw.js` in the browser console are
expected and harmless – the page detects them and falls back to built-in icons.

## Checklist

- [ ] served via HTTPS
- [ ] `*.webmanifest` served as `application/manifest+json` (configs above do this)
- [ ] `index.html` and `sw.js` not cached long (configs above: `no-cache`)
- [ ] after an update, open the site once – the service worker swaps to the new version automatically
