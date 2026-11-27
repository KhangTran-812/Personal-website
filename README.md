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
resume.pdf    # downloadable resume
tests/        # portfolio accessibility checks (pytest)
images/       # portrait, favicon.svg, projects/*.png real app screenshots
```

## Run locally

```bash
python3 -m http.server 8123
# open http://127.0.0.1:8123
```

## Tests

```bash
pip install pytest
pytest tests/
```

## Deploy (GitHub Pages)

Push to `main`; Pages serves from the repo root at
https://khangtran-812.github.io/Personal-website/. The Pages hostname reflects the
upstream repository `KhangTran-812/Personal-website`; `KhangTran69` is the personal
GitHub profile, not a second site.

## Editing notes

- All colors and fonts flow through the `:root` token block in `style.css`
  (hex fallbacks + oklch overrides). Do not add color literals elsewhere.
- Copy follows Hallmark discipline: no em/en dashes, no middle-dot separators,
  no tracked-caps labels, hero headline under 7 words. Keep every metric
  factual and in sync with its source records. The QA figures describe 142 test
  cases run in three environments (426 executions), not overall product quality.
- Project images are real screenshots (`images/projects/`). To recapture the
  Help Desk app: `mvn spring-boot:run -Dspring-boot.run.profiles=h2,demo` in the
  app project, then browse localhost:8080. The optimizer runs with
  `python3 -m streamlit run app.py`. FlowOps: `uvicorn src.api:app`, dashboard
  at `/dashboard`.
- Replace `resume.pdf` with an updated PDF to change the downloadable resume.
- Motion budget: transform/opacity only, reduced-motion fallback required.
