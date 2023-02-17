import unittest
import day4
from day4 import contains
import day5
from day5 import Procedure


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

class TestsDay5(unittest.TestCase):

    def test_read_file(self):
        stacks = dict()
        stacks[1] = ['[Z]', '[N]']
        stacks[2] = ['[M]', '[C]', '[D]']
        stacks[3] = ['[P]']

        procedure = [Procedure(2,1,1), Procedure(1,3,3), Procedure(2,2,1), Procedure(1,1,2)]
        self.assertEqual(day5.read_file('day5t.txt'), (stacks, procedure))

    def test_day5_1(self):
        stacks = dict()
        stacks[1] = ['[C]']
        stacks[2] = ['[M]']
        stacks[3] = ['[P]', '[D]', '[N]', '[Z]']
        self.assertEqual(day5.day5_1('day5t.txt'), stacks)

if __name__ == '__main__':
    unittest.main()