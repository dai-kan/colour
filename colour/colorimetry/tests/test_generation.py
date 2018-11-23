# -*- coding: utf-8 -*-
"""
Defines unit tests for :mod:`colour.colorimetry.generation` module.
"""

from __future__ import division, unicode_literals

import numpy as np
import unittest

from colour.colorimetry.generation import (
    spd_constant, spd_zeros, spd_ones, spd_gaussian_normal, spd_gaussian_fwhm,
    spd_single_led_Ohno2005, multi_led_spd_Ohno2005)

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2018 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = [
    'TestSpdConstant', 'TestZerosSpd', 'TestSpdOnes', 'TestSpdGaussianNormal',
    'TestSpdGaussianFwhm', 'TestSpdSingleLedOhno2005',
    'TestMultiLedSpdOhno2005'
]


class TestSpdConstant(unittest.TestCase):
    """
    Defines :func:`colour.colorimetry.generation.spd_constant` definition unit
    tests methods.
    """

    def test_spd_constant(self):
        """
        Tests :func:`colour.colorimetry.generation.spd_constant` definition.
        """

        spd = spd_constant(np.pi)

        self.assertAlmostEqual(spd[360], np.pi, places=7)

        self.assertAlmostEqual(spd[555], np.pi, places=7)

        self.assertAlmostEqual(spd[780], np.pi, places=7)


class TestZerosSpd(unittest.TestCase):
    """
    Defines :func:`colour.colorimetry.generation.spd_zeros` definition unit
    tests methods.
    """

    def test_zeros_spd(self):
        """
        Tests :func:`colour.colorimetry.generation.spd_zeros`
        definition.
        """

        spd = spd_zeros()

        self.assertEqual(spd[360], 0)

        self.assertEqual(spd[555], 0)

        self.assertEqual(spd[780], 0)


class TestSpdOnes(unittest.TestCase):
    """
    Defines :func:`colour.colorimetry.generation.spd_ones` definition unit
    tests methods.
    """

    def test_spd_ones(self):
        """
        Tests :func:`colour.colorimetry.generation.spd_ones` definition.
        """

        spd = spd_ones()

        self.assertEqual(spd[360], 1)

        self.assertEqual(spd[555], 1)

        self.assertEqual(spd[780], 1)


class TestSpdGaussianNormal(unittest.TestCase):
    """
    Defines :func:`colour.colorimetry.generation.spd_gaussian_normal`
    definition unit tests methods.
    """

    def test_spd_gaussian_normal(self):
        """
        Tests :func:`colour.colorimetry.generation.spd_gaussian_normal`
        definition.
        """

        spd = spd_gaussian_normal(555, 25)

        self.assertAlmostEqual(spd[530], 0.606530659712633, places=7)

        self.assertAlmostEqual(spd[555], 1, places=7)

        self.assertAlmostEqual(spd[580], 0.606530659712633, places=7)


class TestSpdGaussianFwhm(unittest.TestCase):
    """
    Defines :func:`colour.colorimetry.generation.spd_gaussian_fwhm` definition
    unit tests methods.
    """

    def test_spd_gaussian_fwhm(self):
        """
        Tests :func:`colour.colorimetry.generation.spd_gaussian_fwhm`
        definition.
        """

        spd = spd_gaussian_fwhm(555, 25)

        self.assertAlmostEqual(spd[530], 0.367879441171443, places=7)

        self.assertAlmostEqual(spd[555], 1, places=7)

        self.assertAlmostEqual(spd[580], 0.367879441171443, places=7)


class TestSpdSingleLedOhno2005(unittest.TestCase):
    """
    Defines :func:`colour.colorimetry.generation.spd_single_led_Ohno2005`
    definition unit tests methods.
    """

    def test_spd_single_led_Ohno2005(self):
        """
        Tests :func:`colour.colorimetry.generation.spd_single_led_Ohno2005`
        definition.
        """

        spd = spd_single_led_Ohno2005(555, 25)

        self.assertAlmostEqual(spd[530], 0.127118445056538, places=7)

        self.assertAlmostEqual(spd[555], 1, places=7)

        self.assertAlmostEqual(spd[580], 0.127118445056538, places=7)


class TestMultiLedSpdOhno2005(unittest.TestCase):
    """
    Defines :func:`colour.colorimetry.generation.multi_led_spd_Ohno2005`
    definition unit tests methods.
    """

    def test_multi_led_spd_Ohno2005(self):
        """
        Tests :func:`colour.colorimetry.generation.multi_led_spd_Ohno2005`
        definition.
        """

        spd = multi_led_spd_Ohno2005(
            np.array([457, 530, 615]),
            np.array([20, 30, 20]),
            np.array([0.731, 1.000, 1.660]),
        )

        self.assertAlmostEqual(spd[500], 0.129513248576116, places=7)

        self.assertAlmostEqual(spd[570], 0.059932156222703, places=7)

        self.assertAlmostEqual(spd[640], 0.116433257970624, places=7)

        spd = multi_led_spd_Ohno2005(
            np.array([457, 530, 615]),
            np.array([20, 30, 20]),
        )

        self.assertAlmostEqual(spd[500], 0.130394510062799, places=7)

        self.assertAlmostEqual(spd[570], 0.058539618824187, places=7)

        self.assertAlmostEqual(spd[640], 0.070140708922879, places=7)


if __name__ == '__main__':
    unittest.main()
