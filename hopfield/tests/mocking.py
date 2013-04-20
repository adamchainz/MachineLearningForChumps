# coding=utf-8
from ..net import HopfieldNet


def make_net_from_lecture_slides():
    net = HopfieldNet(num_nodes=5)
    net.set_weight(1, 2, -4)
    net.set_weight(1, 3, 3)
    net.set_weight(1, 4, 2)
    net.set_weight(2, 4, 3)
    net.set_weight(2, 5, 3)
    net.set_weight(3, 4, -1)
    net.set_weight(4, 5, -1)

    net.set_nodes([True, False, True, False, False])

    return net
