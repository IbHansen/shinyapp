# Test of the Shiny widgets which the published app does not use (sumslide, sheet)
# and of more result viewer options. Not exported to GitHub Pages.
#
#   C:\deploy\shinyapp\run_test.cmd

from pathlib import Path

from modelclass import model
from modelinput_shiny import make_app

DATA = Path(__file__).parent.parent / 'app' / 'data' / 'pak.pcim'

GGexp = ('PAKGGREVOTHRCN PAKGGEXPCAPTCN PAKGGEXPGNFSCN PAKGGEXPTRNSCN PAKGGEXPOTHRCN '
         'PAKNEGDIFGOVXN PAKBXFSTREMTCD PAKBMFSTREMTCD')


def load_model():
    mpak, bline = model.modelload(str(DATA), start=2023, end=2040, run=True, keep='Baseline')
    mpak.basedf = mpak.fix(bline, GGexp)
    return mpak


co2_common = {'value': 0.0, 'min': -50.0, 'max': 50.0, 'step': 1.0, 'op': '+'}

co2_content = {
    'Coal': {'var': 'PAKGGREVCO2CER', **co2_common},
    'Gas':  {'var': 'PAKGGREVCO2GER', **co2_common},
    'Oil':  {'var': 'PAKGGREVCO2OER', **co2_common},
}

# the same sliders twice, to compare the layouts. Both are applied on a run,
# so with op '+' the two values for a variable add up.
co2_one_column = ['slide', {
    'heading': 'CO2 tax rate changes, columns: 1',
    'columns': 1,          # Shiny only: one slider per row, like the notebook
    'content': co2_content,
}]

co2_auto_columns = ['slide', {
    'heading': 'CO2 tax rate changes, columns not set',
    'content': co2_content,
}]

co2_slidedef = ['base', {'content': [co2_one_column, co2_auto_columns]}]

# a 20 point CO2 tax rise split between the fuels; Oil absorbs the changes
split_def = ['sumslide', {
    'heading': 'Split of a 20 point CO2 tax rise',
    'maxsum': 20.0,
    'content': {
        'Coal': {'var': 'PAKGGREVCO2CER', 'value': 10.0, 'min': 0.0, 'max': 20.0, 'step': 1.0, 'op': '+'},
        'Gas':  {'var': 'PAKGGREVCO2GER', 'value': 5.0,  'min': 0.0, 'max': 20.0, 'step': 1.0, 'op': '+'},
        'Oil':  {'var': 'PAKGGREVCO2OER', 'value': 5.0,  'min': 0.0, 'max': 20.0, 'step': 1.0, 'op': '+',
                 'slack': 'yes'},
    }
}]

# CO2 tax rate added year by year
sheet_def = ['sheet', {
    'heading': 'CO2 tax rate added per year',
    'content': {
        'update_col': ['PAKGGREVCO2CER', 'PAKGGREVCO2GER', 'PAKGGREVCO2OER'],
        'update_index': list(range(2025, 2031)),
        'dec': 1,
        'operator': '+',
    },
    'trans': {'PAKGGREVCO2CER': 'Coal', 'PAKGGREVCO2GER': 'Gas', 'PAKGGREVCO2OER': 'Oil'},
}]

tabdef = ['tab', {
    'content': [
        ('CO2 tax',            co2_slidedef),
        ('Split (sumslide)',   split_def),
        ('Per year (sheet)',   sheet_def),
    ]
}]

app = make_app(tabdef, model_factory=load_model, title='Test: sumslide, sheet and viewer options',
               varpat='*', selected='PAKNYGDPMKTPKN', use_smpl=True, legend=True)
