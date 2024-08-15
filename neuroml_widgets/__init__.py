import logging
import os
import typing

try:
    import importlib.metadata

    __version__ = importlib.metadata.version("neuroml_widgets")
except ImportError:
    import importlib_metadata

    __version__ = importlib_metadata.version("neuroml_widgets")
