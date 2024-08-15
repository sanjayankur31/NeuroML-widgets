#!/usr/bin/env python3
"""
Copyright 2024 NeuroML contributors
"""

import logging
import unittest

import neuroml
from neuroml.utils import component_factory

from neuroml_widgets.component import component2widget

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class TestComponents(unittest.TestCase):
    """Tests for components module"""

    def test_components2widget(self):
        """Test components2widget function"""
        nml_doc = component_factory(neuroml.NeuroMLDocument, id="test")
        component2widget(nml_doc)
        self.assertIsNotNone(nml_doc)
