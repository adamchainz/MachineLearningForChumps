# coding=utf-8
from ..settler import HopfieldSettler

from bases import HopfieldTestCase
from mocking import make_net_from_lecture_slides


class HopfieldSettlerTests(HopfieldTestCase):

    def test_at_energy_minimum(self):
        net = make_net_from_lecture_slides()
        settler = HopfieldSettler(net)
        self.assertFalse(settler.at_energy_minimum())
        HopfieldSettler(net).settle()
        self.assertTrue(settler.at_energy_minimum())

    def test_finding_deep_minimum(self):
        net = make_net_from_lecture_slides()

        net.set_nodes([False, True, False, True, True])
        HopfieldSettler(net).settle()
        self.assertEqual(net.get_total_energy(), -5)
        self.assertEqual(net.get_nodes(), [False, True, False, True, True])
