import unittest
import day4
from day4 import contains


class TestsDay4(unittest.TestCase):

    def test_day4_1(self):
        self.assertEqual(day4.day4_1("day4t.txt"), 2)

    def test_day4_2(self):
        self.assertEqual(day4.day4_2("day4t.txt"), 4)

    def test_contained_1_in_2a(self):
        self.assertTrue(contains((20, 30), (15, 35)))

    def test_contained_1_in_2b(self):
        self.assertTrue(contains((20, 30), (20, 35)))

    def test_contained_1_in_2c(self):
        self.assertTrue(contains((20, 30), (15, 30)))

    def test_contained_1_in_2d(self):
        self.assertTrue(contains((20, 20), (15, 30)))

    def test_contained_2_in_1a(self):
        self.assertTrue(contains((14, 55), (27, 32)))

    def test_contained_2_in_1b(self):
        self.assertTrue(contains((27, 55), (27, 32)))

    def test_contained_2_in_1c(self):
        self.assertTrue(contains((14, 32), (27, 32)))

    def test_contained_2_in_1d(self):
        self.assertTrue(contains((14, 32), (27, 27)))

    def test_contained_equal(self):
        self.assertTrue(contains((14, 14), (14, 14)))

    def test_not_contained_lower(self):
        self.assertFalse(contains((14, 32), (39, 57)))

    def test_not_contained_higher(self):
        self.assertFalse(contains((81, 120), (39, 57)))

    def test_not_contained_equal(self):
        self.assertFalse(contains((81, 81), (39, 39)))

if __name__ == '__main__':
    unittest.main()