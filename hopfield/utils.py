# coding=utf-8
import numpy


def binary_array(ones_zeros):
    array = numpy.zeros(len(ones_zeros), dtype=numpy.int8)
    for i, digit in enumerate(ones_zeros):
        if digit == '1':
            array[i] = 1
    return array


def random_binary_array(length):
    return numpy.random.random_integers(0, 1, length)


def string_to_binary_array(string):
    return binary_array(
        ''.join([bin(ord(i))[2:].rjust(8, '0')
                 for i in string])
    )
