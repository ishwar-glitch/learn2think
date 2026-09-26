# Deploy note (Cloudflare Pages)

Nothing is connected yet. When the founder creates the Pages project, use:

| Setting | Value |
|---|---|
| Production branch | `main` |
| Root directory | `app` |
| Framework preset | Astro |
| Build command | `npm run build` |
| Build output directory | `dist` |
| Environment variable | `NODE_VERSION` = `22` |
| Environment variables | the six `PUBLIC_FIREBASE_*` values from `.env.example`, filled with the real Firebase web-app config |

Note: content is read from `../content`, so the Pages project must build from the whole repo (root directory `app` is fine; the repo is still fully checked out).
Add the Pages domain to Firebase Auth > Settings > Authorized domains.
