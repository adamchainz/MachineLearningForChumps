# coding=utf-8
from ..settler import HopfieldSettler
from ..utils import binary_array

from bases import HopfieldTestCase
from mocking import make_net_from_lecture_slides


class HopfieldSettlerTests(HopfieldTestCase):

    def test_finding_deep_minimum(self):
        net = make_net_from_lecture_slides()

        net.set_nodes(binary_array('01010'))
        self.assertEqual(net.get_total_energy(), -3)
        HopfieldSettler(net).settle()
        self.assertEqual(net.get_total_energy(), -5)
        self.assertArrayEqual(net.get_nodes(), binary_array('01011'))
