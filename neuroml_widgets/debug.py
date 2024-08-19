"""
Debugging utils

File: neuroml_widgets/debug.py

Copyright 2024 NeuroML contributors
"""

import ipywidgets

# https://ipywidgets.readthedocs.io/en/latest/examples/Output%20Widget.html#debugging-errors-in-callbacks-with-the-output-widget
debug_view = ipywidgets.Output(layout={"border": "1px solid black"})
