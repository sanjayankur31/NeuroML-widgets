"""
Widgets for NeuroML simulations

File: neuroml_widgets/simulation.py

Copyright 2024 NeuroML contributors
"""

import logging
import typing
from datetime import datetime
from pathlib import Path

import ipywidgets
from IPython.display import display
from pyneuroml.io import read_lems_file
from pyneuroml.runners import run_lems_with
from pyneuroml.utils.units import split_nml2_quantity

from .debug import debug_view as sim_debug_view

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

logger.debug(f"Logger setup for {__name__}")


sim_widget_states: typing.Dict[str, typing.Tuple[str, str]] = {}
simdata = None


def simulation_manager(simfile: str):
    """Simulation manager widget.

    This allows changing the step, length, seed of a simulation and re-running
    it after generating a new LEMS file.

    :param simfile: complete path to simulation LEMS file
    :type simfile: str
    """
    model = read_lems_file(simfile)
    print(model.toxml())
    simdict = {}

    for am in model.components:
        if am.type == "Simulation":
            simdict = am.parameters

    logger.debug(f"Simdict is {simdict}")
    print(f"Simdict is {simdict}")

    @sim_debug_view.capture(clear_output=True)
    def update_object(change):
        """Change handler"""
        # get units from description
        owner_widget = change["owner"]
        owner_widget_description = owner_widget.description
        init_magnitude = float(sim_widget_states[owner_widget_description][0])
        init_units = sim_widget_states[owner_widget_description][1]

        new_magnitude = float(change["new"])
        new_value = f"{new_magnitude} {init_units}"
        # set new values
        print(f"Setting new values: {owner_widget_description}: {new_value}")
        simdict[owner_widget_description] = new_value

        # TODO: indicate change, does not currently work
        try:
            if str(new_magnitude) != str(init_magnitude):
                owner_widget.style.background = "yellow"
        except KeyError:
            pass

    sim_widgets = []
    for at in ["step", "length", "seed"]:
        value, units = split_nml2_quantity(simdict[at])
        widget = ipywidgets.FloatText(
            value=value,
            description=at,
            disabled=False,
            style={"description_width": "initial"},
        )
        widget.observe(update_object, names="value")
        box_widget = ipywidgets.HBox([widget, ipywidgets.Label(units)])
        sim_widgets.append(box_widget)

        # track initial value for changing widget slide when
        # it's changed, and to reset
        if at not in sim_widget_states:
            sim_widget_states[at] = (value, units)

    @sim_debug_view.capture(clear_output=True)
    def save_and_simulate(button):
        """Save and simulate callback"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        new_simfile = f"{timestamp}_{Path(simfile).name}"
        print(model.export_to_dom().toprettyxml())
        model.export_to_file(new_simfile)
        print(f"Saved {new_simfile}, simulating")
        run_lems_with("jneuroml", new_simfile)

    # simulate button
    sim_button = ipywidgets.Button(
        description="Save and simulate",
        disabled=False,
        button_style="success",
        tooltip="Save LEMS simulation file and simulate",
    )
    sim_button.on_click(save_and_simulate)
    sim_widgets.append(sim_button)

    accordion = ipywidgets.Accordion(
        children=[ipywidgets.VBox(sim_widgets)],
        titles=[f"Simulation: {simdict['target']}"],
    )
    display(accordion)
