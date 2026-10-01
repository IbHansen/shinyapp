# Pakistan carbon tax scenarios (ModelFlow + Shiny)

A web app for running scenarios on the Pakistan model. The inputs are the three
tabs of slider widgets from `interactive.ipynb`: CO2 tax, total factor
productivity and government expenditure. Each run is kept as a scenario and
charted against the baseline.

The app runs in two ways:

- **Normal Python** (`shiny run`), for developing.
- **In the browser** with [Shinylive](https://shiny.posit.co/py/docs/shinylive.html).
  Python runs in the visitor's browser with Pyodide, so the site is static files
  and GitHub Pages can host it.

## Layout

| Path | What |
|---|---|
| `app/app.py` | the app: model loading and the widget definitions |
| `app/requirements.txt` | packages Shinylive installs in the browser (`modelflowib`) |
| `app/data/pak.pcim` | the model and data |
| `app/modelwidget_core.py`, `app/modelinput_shiny.py` | **temporary** copies from the modelflow repo, see below |
| `requirements.txt` | build tools: `shiny`, `shinylive` |
| `.github/workflows/deploy.yml` | exports the app and publishes it on GitHub Pages |

## Local use (Windows)

1. `setup_env.cmd` (once): creates the conda env `shinyapp` with Shiny,
   Shinylive, and ModelFlow installed editable from `C:\modelflow2\modelflow`.
2. `run.cmd`: runs the app with normal Python and opens the browser.
3. `build.cmd`, then `serve.cmd`: exports the browser version to `site\` and
   serves it on http://localhost:8008/. This is what GitHub Pages will show.

## GitHub Pages

Push the folder to a GitHub repo. Then, in the repo settings, go to
**Settings -> Pages -> Build and deployment** and set **Source** to
**GitHub Actions**. Every push to `main` exports and deploys the app.

## Temporary module copies

`modelwidget_core.py` and `modelinput_shiny.py` are new in ModelFlow and not yet
in the released `modelflowib` on PyPI (2.83). Until they are, the app carries
copies next to `app.py`. `sync_modules.cmd`, which `run.cmd` and `build.cmd`
call, refreshes them from the local repo.

Commit the copies, because the GitHub action has no access to the local repo.
Once `modelflowib` 2.84 or later is on PyPI:

- delete the two copies,
- remove the `sync_modules.cmd` calls from `run.cmd` and `build.cmd`.

## Notes

- The first visit downloads Python, pandas and the other packages (tens of MB),
  so it takes a while before the app responds. Later visits use the browser cache.
- Everything runs in the visitor's browser, so the model, data and code are
  visible to anyone who opens the page.
