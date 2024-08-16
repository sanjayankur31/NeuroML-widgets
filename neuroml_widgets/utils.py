"""
Utility widgets for NeuroML

File: neuroml_widgets/utils.py

Copyright 2024 NeuroML contributors.
"""

from ipyfilechooser import FileChooser


def nml_file_chooser(default: str = ""):
    """Choose a NeuroML file.

    Wraps around ipyfilechooser.

    :returns: a file chooser widget instance
    """
    chooser = FileChooser(
        path=".",
        filename=default,
        title="Choose  NeuroML file",
        filter_pattern="*.nml",
        show_hidden=False,
    )
    return chooser


def lems_file_chooser(default: str = ""):
    """Choose a LEMS file.

    Wraps around ipyfilechooser.

    :returns: a file chooser widget instance
    """
    chooser = FileChooser(
        path=".",
        filename=default,
        title="Choose LEMS file",
        filter_pattern="LEMS*xml",
        show_hidden=False,
    )
    return chooser
