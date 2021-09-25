import unittest

from package import module

# TODO:
# https://pythonworld.ru/moduli/modul-unittest.html


class TestPackageModule(unittest.TestCase):
    def test_func_1(self):
        self.assertEqual(3, module.func_1(2, 1))

    def test_func_2(self):
        self.assertEqual(9, module.func_2(3, 3))