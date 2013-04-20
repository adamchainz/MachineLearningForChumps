# coding=utf-8
import unittest


class HopfieldTestCase(unittest.TestCase):
    def assertArrayEqual(self, a, b, message=None):
        self.assertListEqual(list(a), list(b), message)
