"""
Widgets for NeuroML simulations

File: neuroml_widgets/simulation.py

Copyright 2024 NeuroML contributors
"""

import logging

import ipywidgets
from pyneuroml.io import read_lems_file

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

logger.debug(f"Logger setup for {__name__}")


def simulation_manager(simfile: str):
    """Simulation manager widget.

    This allows changing the step, length, seed of a simulation and re-running
    it after generating a new LEMS file.

    :param simfile: complete path to simulation LEMS file
    :type simfile: str
    """
    model = read_lems_file(simfile)
    simdict = {}

    for am in model.components:
        if am.type == "Simulation":
            simdict = am.parameters

    logger.debug(f"Simdict is {simdict}")
    # TODO: create widget and run button etc.print(simdict)
    # TODO: is this the best way, or should I be reading the file as XML so
    # that we don't lose the other bits?
