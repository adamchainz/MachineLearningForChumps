# coding=utf-8
from ..utils import binary_array, string_to_binary_array

from bases import HopfieldTestCase


class UtilsTests(HopfieldTestCase):

    def test_binary_array(self):
        self.assertArrayEqual(
            binary_array('10'),
            [1, 0]
        )

    def test_string_to_binary_array(self):
        bin_dog = string_to_binary_array('dog')

        self.assertEqual(len(bin_dog), 24)

        self.assertArrayEqual(
            bin_dog,
            [0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
        )
