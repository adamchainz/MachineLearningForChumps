# coding=utf-8


def binary_array(ones_zeros):
    return [digit == '1' for digit in ones_zeros]


def string_to_binary_array(string):
    return binary_array(''.join(['%08d' % int(bin(ord(i))[2:]) for i in string]))
