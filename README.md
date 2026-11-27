# Personal Website

Portfolio of **Khang B. Tran** — CS student and QA intern (Angeles City, PH).

Plain HTML/CSS/JS, no build step. Design direction: **Hallmark "Terminal" material**
(adapted from [Nutlope/hallmark](https://github.com/Nutlope/hallmark), MIT): dark
green-tinted paper, Martian Mono as the single type family, terminal-green accent,
hairline rules, zero radius, no shadows or glow, one accent color.

## Structure

```
index.html    # hero, about, projects, skills, experience, contact
style.css     # Hallmark stamp comment, full token system, Terminal material
script.js     # mobile nav, scrollspy, footer year (no auto-playing motion)
resume.pdf    # downloadable resume (generated from the fixed DOCX)
images/       # portrait, favicon.svg, projects/*.png real app screenshots
```

## Run locally

```bash
python3 -m http.server 8123
# open http://127.0.0.1:8123
```

## Deploy (GitHub Pages)

Push to `main`; Pages serves from the repo root at
https://khangtran-812.github.io/Personal-website/.

## Editing notes

- All colors and fonts flow through the `:root` token block in `style.css`
  (hex fallbacks + oklch overrides). Do not add color literals elsewhere.
- Copy follows Hallmark discipline: no em/en dashes, no middle-dot separators,
  no tracked-caps labels, hero headline under 7 words, page under ~450 words.
  Keep every metric factual and in sync with the resume.
- Project images are real screenshots (`images/projects/`). To recapture the
  Help Desk app: `mvn spring-boot:run -Dspring-boot.run.profiles=h2,demo` in the
  app project, then browse localhost:8080. The optimizer runs with
  `python3 -m streamlit run app.py` (Streamlit UI needs real clicks, not synthetic ones).
- Motion budget: transform/opacity only, reduced-motion fallback required.
