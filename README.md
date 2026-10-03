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
| `app/requirements.txt` | packages Shinylive installs in the browser (`modelflowib>=2.85` and its Pyodide dependencies) |
| `app/data/pak.pcim` | the model and data |
| `test_app/app.py` | test of the widgets the app does not use (`sumslide`, `sheet`); not published |
| `requirements.txt` | build tools: `shiny`, `shinylive` |
| `.github/workflows/deploy.yml` | exports the app and publishes it on GitHub Pages |

The Shiny code (`modelinput_shiny`, `modelwidget_core`) is part of ModelFlow
from version 2.84.

## Local use (Windows)

1. `setup_env.cmd` (once): creates the conda env `shinyapp` with Shiny,
   Shinylive, and ModelFlow installed editable from `C:\modelflow2\modelflow`.
2. `run.cmd` (double-click): runs the app with normal Python and opens the
   browser at http://127.0.0.1:8000. Close its window to stop the app.
   `run_test.cmd` does the same for the test app, on port 8001.
3. `build.cmd`, then `serve.cmd`: exports the browser version to `site\` and
   serves it on http://localhost:8008/. This is what GitHub Pages will show.

Locally the app uses ModelFlow from `C:\modelflow2\modelflow` (the editable
install), so changes there show up at once. The browser version uses the
`modelflowib` released on PyPI.

## GitHub Pages

Push the folder to a GitHub repo. Then, in the repo settings, go to
**Settings -> Pages -> Build and deployment** and set **Source** to
**GitHub Actions**. Every push to `main` exports and deploys the app.

## Notes

- The first visit downloads Python, pandas and the other packages (tens of MB),
  so it takes a while before the app responds. Later visits use the browser cache.
- Everything runs in the visitor's browser, so the model, data and code are
  visible to anyone who opens the page.
