"""
General widgets for use with all NeuroML components.

File: neuroml_widgets/component.py

Copyright 2024 NeuroML contributors
"""

import logging
import typing

import ipywidgets
import neuroml

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

logger.debug(f"Logger setup for {__name__}")


def component_explorer(
    component: neuroml.nml.nml.GeneratedsSuperSuper,
    max_members: int = 10,
    tabbed_list: typing.List[str] = [],
):
    """Create a widget from a NeuroML component object.

    Recursively explore a NeuroML component.

    :param component: NeuroML component object to explore
    :type component: object
    :param max_members: how many members to show when there are many
    :type max_members: int
    :param tabbed_list: list of Component Type class names to organise in tabs,
        all others are put in a "Other" tab. If this is empty, everything is
        listed as an accordion in a "flat" structure
    :type tabbed_list: list of strings
    :returns: widget object

    """
    logger.debug(f"Processing {component.__class__.__name__}")
    members = component.info(show_contents=True, return_format="dict")
    logger.debug(f"Members are {members}")
    try:
        if members["id"] is not None:
            title = f"{component.__class__.__name__}: {members.pop('id')['members']}"
        else:
            title = f"{component.__class__.__name__}"
    except KeyError:
        title = f"{component.__class__.__name__}"
    logger.debug(f"Got title: {title}")

    field_members = []
    accordion_widgets = []
    # need to be processed together later
    tabbed_widgets = {}
    for m, contents in members.items():
        # can either be a string, or an object, or a list of objects
        cont = contents["members"]
        cont_type = contents["type"]
        logger.debug(f"Type is {cont_type}")
        if cont:
            if not isinstance(cont, list):
                if isinstance(cont, (str, float, int)):
                    logger.debug(f"Got a string/float member: {m}")
                    if cont_type.startswith("Nml2Quantity"):
                        escaped_cont = contents["members"].replace("_", "\\_")
                    else:
                        escaped_cont = contents["members"]
                    field_members.append(f"<li><b>{m}</b>: {escaped_cont}</li>")
                elif isinstance(cont, object):
                    logger.debug(f"Got an object member: {m}")
                    accordion_widgets.append(
                        component_explorer(
                            contents["members"], max_members, tabbed_list
                        )
                    )
                else:
                    logger.error(f"What did we get? {m}")
            else:
                logger.debug(f"Got list member: {m} ({len(cont)} members)")
                processed_members = 0
                multi_widgets = []
                for x in cont:
                    if processed_members < max_members:
                        logger.debug(f"Processing list member: {m}")
                        multi_widgets.append(
                            component_explorer(x, max_members, tabbed_list)
                        )
                    else:
                        field_members.append(
                            f"<li><b>{m}</b>: {len(cont)} members (showing {max_members})</li>"
                        )
                        break
                    processed_members += 1
                if cont_type in tabbed_list:
                    tabbed_widgets[cont_type] = ipywidgets.VBox(multi_widgets)
                else:
                    accordion_widgets.extend(multi_widgets)

    widgets = []
    if len(field_members) > 0:
        fields_html_string = ""
        fields_html_string += "<ul>"
        for m in field_members:
            fields_html_string += m
        fields_html_string += "</ul></br>"

        widgets.append(ipywidgets.HTMLMath(value=fields_html_string))

    # if tabs are in use, put the untabbed ones in a new "other" tab
    if len(tabbed_widgets) > 0:
        tabbed_widgets["Other"] = ipywidgets.VBox(accordion_widgets)
        titles = []
        # add number of entries to each tab title
        for k, v in tabbed_widgets.items():
            titles.append(f"{k} ({len(v.children)})")

        widgets.append(
            ipywidgets.Tab(
                children=list(tabbed_widgets.values()),
                titles=titles,
            )
        )
    # otherwise, use a flat list of accordions
    else:
        widgets.extend(accordion_widgets)

    widgets = [x for x in widgets if x is not None]

    if len(widgets) > 0:
        logger.debug(widgets)
        logger.debug(f"There are {len(widgets)} widgets")

    return (
        ipywidgets.Accordion(children=[ipywidgets.VBox(widgets)], titles=[title])
        if len(widgets) > 0
        else None
    )
