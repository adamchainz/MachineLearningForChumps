# coding=utf-8
import unittest

from ..net import HopfieldNet

from mocking import make_net_from_lecture_slides


class HopfieldNetTests(unittest.TestCase):
    def test_weight_setting(self):
        net = HopfieldNet(num_nodes=2)
        net.set_weight(1, 2, weight=4)
        self.assertEqual(net.get_weight(1, 2), 4)
        self.assertEqual(net.get_weight(2, 1), 4)
        net.set_weight(2, 1, weight=5)
        self.assertEqual(net.get_weight(2, 1), 5)
        self.assertEqual(net.get_weight(1, 2), 5)

    def test_node_setting(self):
        net = HopfieldNet(num_nodes=2)
        self.assertEqual(net.get_node(1), False)

        self.assertTrue(net.set_node(1, True))
        self.assertEqual(net.get_node(1), True)
        self.assertFalse(net.set_node(1, True))

        self.assertTrue(net.set_node(1, False))
        self.assertEqual(net.get_node(1), False)
        self.assertFalse(net.set_node(1, False))

    def test_set_nodes(self):
        net = HopfieldNet(num_nodes=2)

        net.set_nodes([True, False])
        self.assertTrue(net.get_node(1))
        self.assertFalse(net.get_node(2))

        with self.assertRaises(AssertionError):
            net.set_nodes([])

        with self.assertRaises(AssertionError):
            net.set_nodes([True])

        with self.assertRaises(AssertionError):
            net.set_nodes([True, True, True])

    def test_get_node_energy_gap(self):
        net = HopfieldNet(num_nodes=3)
        net.set_weight(1, 2, weight=3)
        net.set_weight(1, 3, weight=-1)
        net.set_node(2, True)
        net.set_node(3, False)

        self.assertEqual(net.get_node_energy_gap(1), 3)

        net.set_node(1, True)
        self.assertEqual(net.get_node_energy_gap(1), 3)

        net.set_node(2, False)
        self.assertEqual(net.get_node_energy_gap(1), 0)

    def test_get_total_energy(self):
        net = make_net_from_lecture_slides()

        self.assertEqual(net.get_total_energy(), -3)

        net.set_nodes([False, True, False, True, True])
        self.assertEqual(net.get_total_energy(), -5)
