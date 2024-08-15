"""


File: neuroml_widgets/component.py

Copyright 2024 NeuroML contributors
"""

import ipywidgets
import neuroml


def component2widget(component: neuroml.nml.nml.GeneratedsSuperSuper, recursing=False):
    """Create a widget from a NeuroML component object

    :param component: TODO
    :returns: TODO

    """
    members = component.info(show_contents=True, return_format="dict")
    widgets = []

    try:
        if members["id"] is not None:
            widgets.append(
                ipywidgets.HTML(
                    value=f"<h2>{component.__class__.__name__}: {members.pop('id')['members']}</h2><br>"
                )
            )
    except KeyError:
        widgets.append(
            ipywidgets.HTML(value=f"<h2>{component.__class__.__name__}</h2><br>")
        )

    field_members = []
    container_members = {}
    for m, contents in members.items():
        # can either be a string, or an object, or a list of objects
        cont = contents["members"]
        if cont:
            if not isinstance(cont, list):
                if isinstance(cont, str):
                    field_members.append(f"<li>{m}: {contents['members']}</li>")
                elif isinstance(cont, object):
                    # TODO: figure out how to handle these
                    continue
                    container_members[m] = component2widget(
                        contents["members"], recursing=True
                    )
            else:
                # TODO: figure out how to handle these
                continue
                container_widgets = []
                for x in cont:
                    container_widgets.append(component2widget(x, recursing=True))
                container_members[m] = container_widgets

    if len(field_members) > 0:
        widgets.append(ipywidgets.HTML(value="<ul>"))
        for m in field_members:
            widgets.append(ipywidgets.HTML(value=m))
        widgets.append(ipywidgets.HTML(value="</ul>"))
        widgets.append(ipywidgets.HTML(value="</br>"))

    print(container_members)
    widgets.append(
        ipywidgets.Accordion(
            children=tuple(container_members.values()),
            titles=tuple(container_members.keys()),
        )
    )

    if not recursing:
        return ipywidgets.HBox(widgets)
    else:
        return widgets
