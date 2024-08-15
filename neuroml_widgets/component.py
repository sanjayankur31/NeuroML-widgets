"""


File: neuroml_widgets/component.py

Copyright 2024 NeuroML contributors
"""

import logging

import ipywidgets
import neuroml

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

logger.debug(f"Logger setup for {__name__}")


def component2widget(component: neuroml.nml.nml.GeneratedsSuperSuper, member_limit=10):
    """Create a widget from a NeuroML component object

    :param component: TODO
    :returns: TODO

    """
    logger.debug(f"Processing {component.__class__.__name__}")
    members = component.info(show_contents=True, return_format="dict")
    try:
        if members["id"] is not None:
            title = f"{component.__class__.__name__}: {members.pop('id')['members']}"
        else:
            title = f"{component.__class__.__name__}"
    except KeyError:
        title = f"{component.__class__.__name__}"
    logger.debug(f"Got title: {title}")

    field_members = []
    container_widgets = []
    for m, contents in members.items():
        # can either be a string, or an object, or a list of objects
        cont = contents["members"]
        if cont:
            if not isinstance(cont, list):
                if isinstance(cont, (str, float, int)):
                    logger.debug(f"Got a string/float member: {m}")
                    field_members.append(f"<li><b>{m}</b>: {contents['members']}</li>")
                elif isinstance(cont, object):
                    logger.debug(f"Got an object member: {m}")
                    container_widgets.append(component2widget(contents["members"]))
                else:
                    logger.error(f"What did we get? {m}")
            else:
                logger.debug(f"Got list member: {m} ({len(cont)} members)")
                if len(cont) > member_limit:
                    field_members.append(
                        f"<li><b>{m}</b>: {len(cont)} members (not shown)</li>"
                    )
                else:
                    for x in cont:
                        logger.debug(f"Processing list member: {m}")
                        container_widgets.append(component2widget(x))

    widgets = []
    if len(field_members) > 0:
        fields_html_string = ""
        fields_html_string += "<ul>"
        for m in field_members:
            fields_html_string += m
        fields_html_string += "</ul></br>"

        widgets.append(ipywidgets.HTML(value=fields_html_string))

    widgets.extend(container_widgets)
    widgets = [x for x in widgets if x is not None]

    if len(widgets) > 0:
        logger.debug(widgets)
        logger.debug(f"There are {len(widgets)} widgets")

    return (
        ipywidgets.Accordion(children=[ipywidgets.VBox(widgets)], titles=[title])
        if len(widgets) > 0
        else None
    )
