# coding=utf-8
import numpy


def binary_array(ones_zeros):
    array = numpy.zeros(len(ones_zeros), dtype=numpy.int8)
    for i, digit in enumerate(ones_zeros):
        if digit == '1':
            array[i] = 1
    return array


def string_to_binary_array(string):
    return binary_array(
        ''.join(['%08d' % int(bin(ord(i))[2:])
                 for i in string])
    )
