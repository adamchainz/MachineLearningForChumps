# coding=utf-8
import numpy
import unittest

from ..utils import binary_array


class UtilsTests(unittest.TestCase):
    def test_binary_array(self):
        self.assertItemsEqual(
            binary_array('10'),
            numpy.array([1, 0], dtype=numpy.int8)
        )
