# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from iaia.theme.testing import IAIA_THEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that iaia.theme is properly installed."""

    layer = IAIA_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if iaia.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'iaia.theme'))

    def test_browserlayer(self):
        """Test that IIaiaThemeLayer is registered."""
        from iaia.theme.interfaces import (
            IIaiaThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(IIaiaThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = IAIA_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['iaia.theme'])

    def test_product_uninstalled(self):
        """Test if iaia.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'iaia.theme'))

    def test_browserlayer_removed(self):
        """Test that IIaiaThemeLayer is removed."""
        from iaia.theme.interfaces import \
            IIaiaThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(IIaiaThemeLayer, utils.registered_layers())
