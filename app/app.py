# Pakistan carbon tax scenarios: the widgets from interactive.ipynb as a Shiny app.
#
# Locally:   run.cmd              (shiny run, normal Python)
# Browser:   build.cmd, serve.cmd (shinylive export, runs in the browser with Pyodide)

from pathlib import Path

from modelclass import model
from modelinput_shiny import make_app

HERE = Path(__file__).parent

# Government spending variables to be held constant
GGexp = ('PAKGGREVOTHRCN PAKGGEXPCAPTCN PAKGGEXPGNFSCN PAKGGEXPTRNSCN PAKGGEXPOTHRCN '
         'PAKNEGDIFGOVXN PAKBXFSTREMTCD PAKBMFSTREMTCD')


def load_model():
    mpak, bline = model.modelload(str(HERE / 'data' / 'pak.pcim'), start=2023, end=2040, run=True, keep='Baseline')
    mpak.basedf = mpak.fix(bline, GGexp)   # Freeze other spending levels
    return mpak


co2_common = {'value': 0.0, 'min': -50.0, 'max': 50.0, 'step': 1.0, 'op': '+'}
gov_common = {'value': 0.0, 'min': -2.0, 'max': 2.0, 'step': 0.1, 'op': '+%of', 'divisor': 'PAKNYGDPMKTPCN'}

co2_slidedef = ['slide', {
    'heading': 'CO2 tax rate changes ',
    'content': {
        'Coal': {'var': 'PAKGGREVCO2CER', **co2_common},
        'Gas':  {'var': 'PAKGGREVCO2GER', **co2_common},
        'Oil':  {'var': 'PAKGGREVCO2OER', **co2_common},
    }
}]

tfp_slidedef = ['slide', {
    'heading': 'Total factor productivity, % change ',
    'content': {
        'Total factor productivity': {'var': 'PAKNYGDPTFP', 'value': 0.0, 'min': -50.0, 'max': 50.0, 'step': 1.0, 'op': '%'},
    }
}]

gov_slidedef = ['slide', {
    'heading': 'Government expenditure, % of GDP ',
    'content': {
        'Transfers to households':              {'var': 'PAKGGEXPTRNSCN_X', **gov_common},
        'Gov. expenditure on investment goods': {'var': 'PAKGGEXPCAPTCN_X', **gov_common},
    }
}]

tabdef = ['tab', {
    'content': [
        ('CO2 tax',                    co2_slidedef),
        ('Total factor productivity',  tfp_slidedef),
        ('Government expenditure',     gov_slidedef),
    ]
}]

app = make_app(tabdef, model_factory=load_model, title='Pakistan: carbon tax scenarios',
               varpat='*', selected='PAKNYGDPMKTPKN')
