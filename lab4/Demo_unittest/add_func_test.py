import unittest

from lab4.Demo_unittest.add_function import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(-1, 2), 1)

    def test_bad_input(self):
        with self.assertRaises(TypeError):
            add('a', 1)
        with self.assertRaises(TypeError):
            add(1, 'a')
        with self.assertRaises(TypeError):
            add('a', 'b')


if __name__ == '__main__':
    unittest.main()
