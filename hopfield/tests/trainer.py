# coding=utf-8
import unittest

from ..trainer import HopfieldTrainer

from mocking import make_net_from_lecture_slides


class HopfieldTrainerTests(unittest.TestCase):

    def test_basic(self):
        net = make_net_from_lecture_slides()
        self.assertEqual(net.get_total_energy(), -3)
        HopfieldTrainer(net).settle()
        self.assertEqual(net.get_total_energy(), -4)

    def test_deeper_minimum(self):
        net = make_net_from_lecture_slides()

        net.set_nodes([False, True, False, True, True])
        HopfieldTrainer(net).settle()
        self.assertEqual(net.get_total_energy(), -5)
