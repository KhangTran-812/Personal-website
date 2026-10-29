# Personal Website

Portfolio of **Khang B. Tran** — CS student & aspiring application developer (Angeles City, PH).

Built with plain HTML/CSS/JS — no build step. Dark slate theme, emerald accent,
Poppins / Inter / Roboto Mono via Google Fonts. The hero text is static and the interaction script is optional.

## Structure

```
index.html    # all sections: hero, about, projects, skills, experience, contact
style.css     # theme tokens in :root, responsive at 960px / 760px
script.js     # mobile nav, scrollspy, optional reveal-on-scroll, footer year
resume.pdf    # downloadable resume (generated from the fixed DOCX)
images/       # portrait, favicon, project screenshots and illustrative graphics
```

## Run locally

```bash
python3 -m http.server 8123
# open http://127.0.0.1:8123
```

(Open `index.html` directly also works — no server required.)

## Deploy (GitHub Pages)

Push to `main`; Pages serves from the repo root at
https://khangtran-812.github.io/Personal-website/.

## Editing notes

- Theme colors and fonts are CSS custom properties at the top of `style.css`.
- Project cards live in `index.html` under `#projects`. The garbage optimizer
  and QA suite SVGs are illustrative graphics; PNG/JPG assets are project screenshots.
- Replace images in `images/` and update their paths and intrinsic dimensions in `index.html`.
- Replace `resume.pdf` with an updated PDF to change the downloadable resume. No source DOCX is included here.
- Keep experience and project metrics aligned with their source records. The QA figures describe
  142 test cases run in three environments (426 executions), not overall product quality.
- `KhangTran69` is the personal GitHub profile. The GitHub Pages hostname reflects the upstream
  repository `KhangTran-812/Personal-website`; it is hosting context, not a second personal profile.
