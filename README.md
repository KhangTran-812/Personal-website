# Personal Website

Portfolio of **Khang B. Tran** — CS student & aspiring application developer (Angeles City, PH).

Built with plain HTML/CSS/JS — no build step. Dark slate theme, emerald accent,
Poppins / Inter / Roboto Mono via Google Fonts, Typed.js typing effect.

## Structure

```
index.html    # all sections: hero, about, projects, skills, experience, contact
style.css     # theme tokens in :root, responsive at 960px / 760px
script.js     # typing effect, mobile nav, scrollspy, reveal-on-scroll, footer year
resume.pdf    # downloadable resume (generated from the fixed DOCX)
images/       # portrait, favicon.svg, projects/*.svg preview cards
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
- Project cards live in `index.html` under `#projects`; the preview graphics are
  SVG placeholders in `images/projects/` — swap them for real app screenshots
  (PNG/JPG) when available, keeping the same filenames or updating `src`.
- `resume.pdf`: edit the DOCX source, then regenerate:
  `soffice --headless --convert-to pdf --outdir . <file>.docx` and rename to `resume.pdf`.
- Factual metrics (426 tests, 100% pass rate, 41,575 views…) come from the
  resume — keep them in sync when the resume changes.
