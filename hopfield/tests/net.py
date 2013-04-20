# coding=utf-8
from ..net import HopfieldNet

from bases import HopfieldTestCase
from mocking import make_net_from_lecture_slides


class HopfieldNetTests(HopfieldTestCase):
    def test_weight_setting(self):
        net = HopfieldNet(num_nodes=2)
        net.set_weight(0, 1, weight=4)
        self.assertEqual(net.get_weight(0, 1), 4)
        self.assertEqual(net.get_weight(1, 0), 4)
        net.set_weight(0, 1, weight=5)
        self.assertEqual(net.get_weight(1, 0), 5)
        self.assertEqual(net.get_weight(0, 1), 5)

    def test_node_setting(self):
        net = HopfieldNet(num_nodes=2)
        self.assertEqual(net.get_node(0), False)

        self.assertTrue(net.set_node(0, True))
        self.assertEqual(net.get_node(0), True)
        self.assertFalse(net.set_node(0, True))

        self.assertTrue(net.set_node(0, False))
        self.assertEqual(net.get_node(0), False)
        self.assertFalse(net.set_node(0, False))

    def test_set_nodes(self):
        net = HopfieldNet(num_nodes=2)

        net.set_nodes([True, False])
        self.assertTrue(net.get_node(0))
        self.assertFalse(net.get_node(1))

        with self.assertRaises(AssertionError):
            net.set_nodes([])

        with self.assertRaises(AssertionError):
            net.set_nodes([True])

        with self.assertRaises(AssertionError):
            net.set_nodes([True, True, True])

    def test_get_node_energy_gap(self):
        net = HopfieldNet(num_nodes=3)
        net.set_weight(0, 1, weight=3)
        net.set_weight(0, 2, weight=-1)
        net.set_node(1, True)
        net.set_node(2, False)

        self.assertEqual(net.get_node_energy_gap(0), 3)

        net.set_node(0, True)
        self.assertEqual(net.get_node_energy_gap(0), 3)

        net.set_node(1, False)
        self.assertEqual(net.get_node_energy_gap(0), 0)

    def test_get_total_energy(self):
        net = make_net_from_lecture_slides()

        self.assertEqual(net.get_total_energy(), -3)

        net.set_nodes([False, True, False, True, True])
        self.assertEqual(net.get_total_energy(), -5)
