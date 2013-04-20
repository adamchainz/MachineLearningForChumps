# coding=utf-8
from ..settler import HopfieldSettler
from ..storage import HopfieldStorageNet, HopfieldStringStorageNet
from ..utils import binary_array, string_to_binary_array

from bases import HopfieldTestCase
from mocking import all_binary_arrays


class HopfieldStorageNetTests(HopfieldTestCase):
    def test_init_with_bad_lengths_impossible(self):
        memories = [
            binary_array('01'),
            binary_array('0')
        ]
        with self.assertRaises(AssertionError):
            HopfieldStorageNet(memories)

    def test_memories_stored(self):
        memories = [
            binary_array('10101'),
            binary_array('01010')
        ]
        net = HopfieldStorageNet(memories)

        strung_up_memories = [str(m) for m in memories]

        for array in all_binary_arrays(5):
            net.set_nodes(array)
            HopfieldSettler(net).settle()
            self.assertIn(str(net.nodes), strung_up_memories)


class HopfieldStringStorageNetTests(HopfieldTestCase):
    def assertArrayEqual(self, a, b, message=None):
        self.assertListEqual(list(a), list(b), message)

    def check_word(self, net, word):
        arr = string_to_binary_array(word)
        self.assertArrayEqual(net.get_nodes(), arr)

    def test_init(self):
        net = HopfieldStringStorageNet(['dog', 'cat'])

        self.assertEqual(net.num_nodes, 8 * 3)

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
