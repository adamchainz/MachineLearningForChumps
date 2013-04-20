# coding=utf-8
import unittest

from ..settler import HopfieldSettler
from ..storage import HopfieldStorageNet, HopfieldStringStorageNet
from ..utils import binary_array, string_to_binary_array

from mocking import all_binary_arrays


class HopfieldStorageNetTests(unittest.TestCase):
    def test_init_with_bad_lengths_impossible(self):
        memories = [
            binary_array('00000'),
            binary_array('0000')
        ]
        with self.assertRaises(AssertionError):
            HopfieldStorageNet(memories)

    def test_memories_stored(self):
        memories = [
            binary_array('10101'),
            binary_array('01010')
        ]
        net = HopfieldStorageNet(memories)

        for array in all_binary_arrays(5):
            net.set_nodes(array)
            HopfieldSettler(net).settle()
            self.assertIn(net.get_nodes(), memories)


class HopfieldStringStorageNetTests(unittest.TestCase):
    def check_word(self, net, word):
        arr = string_to_binary_array(word)
        self.assertEqual(net.get_nodes(), arr)

    def test_init(self):
        net = HopfieldStringStorageNet(['dog', 'cat'])

        for word in ('dag', 'dig', 'dug', 'hog'):
            arr = string_to_binary_array(word)
            net.set_nodes(arr)
            HopfieldSettler(net).settle()
            self.check_word(net, 'dog')

        for word in ('hat', 'czt', 'caa'):
            arr = string_to_binary_array(word)
            net.set_nodes(arr)
            HopfieldSettler(net).settle()
            self.check_word(net, 'cat')
