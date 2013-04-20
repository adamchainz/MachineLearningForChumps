# coding=utf-8
from ..utils import binary_array
from ..net import HopfieldNet


def binary_string(array):
    return ''.join([int(x) for x in array])


def padded(binary_array, num_digits):
    return (
        [False] * (num_digits - len(binary_array)) +
        binary_array
    )


def all_binary_arrays(num_digits):
    for i in xrange(2 ** num_digits):
        string = bin(i)[2:].rjust(num_digits, '0')
        yield binary_array(string)


def make_net_from_lecture_slides():
    net = HopfieldNet(num_nodes=5)
    net.set_weight(0, 1, -4)
    net.set_weight(0, 2, 3)
    net.set_weight(0, 3, 2)
    net.set_weight(1, 3, 3)
    net.set_weight(1, 4, 3)
    net.set_weight(2, 3, -1)
    net.set_weight(3, 4, -1)

    net.set_nodes([True, False, True, False, False])

    return net
