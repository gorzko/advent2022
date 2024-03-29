import unittest
import day4
from day4 import contains
import day5
from day5 import Procedure
import day6
import day7
from day7 import Directory, DirectoriesCollection
import day8
import day9
import day10
import day11
import day12
import day12b
import day13
import day14
import day15
import day16
import day17
import day18
import day19

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
        self.assertEqual(day5.day5_1('day5t.txt'), 'CMZ')

    def test_day5_2(self):
        self.assertEqual(day5.day5_2('day5t.txt'), 'MCD')

class TestDay6(unittest.TestCase):

    def test_day6_1a(self):
        self.assertEqual(day6.day6('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4), 7)
    def test_day6_1b(self):
        self.assertEqual(day6.day6('bvwbjplbgvbhsrlpgdmjqwftvncz', 4), 5)
    def test_day6_1c(self):
        self.assertEqual(day6.day6('nppdvjthqldpwncqszvftbrmjlhg', 4), 6)
    def test_day6_1d(self):
        self.assertEqual(day6.day6('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4), 10)
    def test_day6_1e(self):
        self.assertEqual(day6.day6('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4), 11)

    def test_day6_2a(self):
        self.assertEqual(day6.day6('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14), 19)

    def test_day6_2b(self):
        self.assertEqual(day6.day6('bvwbjplbgvbhsrlpgdmjqwftvncz', 14), 23)

    def test_day6_2c(self):
        self.assertEqual(day6.day6('nppdvjthqldpwncqszvftbrmjlhg', 14), 23)

    def test_day6_2d(self):
        self.assertEqual(day6.day6('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14), 29)

    def test_day6_2e(self):
        self.assertEqual(day6.day6('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14), 26)

class TestDay7(unittest.TestCase):

    def test_read_file(self):
        main = Directory('/', DirectoriesCollection())
        a = Directory('a', DirectoriesCollection())
        e = Directory('e', DirectoriesCollection())
        d = Directory('d', DirectoriesCollection())
        main.add_child(a)
        main.add_child(d)
        a.add_child(e)
        e.add_file(('i', 584))
        a.add_file(('f', 29116))
        a.add_file(('g', 2557))
        a.add_file(('h.lst', 62596))
        main.add_file(('b.txt', 14848514))
        main.add_file(('c.dat', 8504156))
        d.add_file(('j', 4060174))
        d.add_file(('d.log', 8033020))
        d.add_file(('d.ext', 5626152))
        d.add_file(('k', 7214296))
        directories = DirectoriesCollection()
        directories.add(main)
        directories.add(a)
        directories.add(e)
        directories.add(d)
        self.assertEqual(day7.read_file('day7t.txt'), directories)

    def test_day7_1(self):
        self.assertEqual(day7.day7_1('day7t.txt'), 95437)

    def test_day7_2(self):
        self.assertEqual(day7.day7_2('day7t.txt'), 24933642)

class TestDay8(unittest.TestCase):
    l = [[3, 0, 3, 7, 3],
         [2, 5, 5, 1, 2],
         [6, 5, 3, 3, 2],
         [3, 3, 5, 4, 9],
         [3, 5, 3, 9, 0]]
    def test_read_file(self):
        self.assertEqual(day8.read_file('day8t.txt'), self.l)

    def test_check_vertically1(self):
        self.assertTrue(day8.check_vertically(self.l, 1, 2))

    def test_check_vertically2(self):
        self.assertFalse(day8.check_vertically(self.l, 2, 1))

    def test_check_vertically3(self):
        self.assertFalse(day8.check_vertically(self.l, 2, 2))

    def test_check_vertically4(self):
        self.assertFalse(day8.check_vertically(self.l, 3, 1))

    def test_check_vertically5(self):
        self.assertFalse(day8.check_vertically(self.l, 3, 3))

    def test_check_vertically6(self):
        self.assertTrue(day8.check_vertically(self.l, 3, 2))

    def test_count_visible(self):
        self.assertEqual(day8.count_visible(self.l), 5)

    def test_day8_1(self):
        self.assertEqual(day8.day8_1('day8t.txt'), 21)

    def test_calculate_scenic_score1(self):
        self.assertEqual(day8.calculate_scenic_score(self.l, 1, 2), 4)

    def test_calculate_scenic_score2(self):
        self.assertEqual(day8.calculate_scenic_score(self.l, 3, 2), 8)

    def test_calculate_scenic_score3(self):
        self.assertEqual(day8.calculate_scenic_score(self.l, 3, 4), 0)

    def test_day_8_2(self):
        self.assertEqual(day8.day8_2('day8t.txt'), 8)

class TestDay9(unittest.TestCase):

    def test_day9_1(self):
        self.assertEqual(day9.day9('day9t.txt', 2), ((3, 3), (2, 3), 13))

    def test_day9_2(self):
        self.assertEqual(day9.day9('day9t.txt', 10), ((3, 3), (1, 1), 1))

    def test_day9_2b(self):
        self.assertEqual(day9.day9('day9t2.txt', 10), ((-10, 16), (-10, 7), 36))

class TestDay10(unittest.TestCase):

    def test_day10_1(self):
        self.assertEqual(day10.day10_1('day10t.txt'), 13140)

    def test_day10_2(self):
        output = '##..##..##..##..##..##..##..##..##..##..\n\
###...###...###...###...###...###...###.\n\
####....####....####....####....####....\n\
#####.....#####.....#####.....#####.....\n\
######......######......######......####\n\
#######.......#######.......#######.....\n'
        self.assertEqual(day10.day10_2('day10t.txt'), output)

class TestDay11(unittest.TestCase):

    def test_day11_1(self):
        self.assertEqual(day11.day11('day11t.txt', 20, 3), 10605)

    # def test_day11_2(self):
    #     self.assertEqual(day11.day11('day11t.txt', 10000, 0), 2713310158)

class TestDay12(unittest.TestCase):

    def test_day12_1(self):
        self.assertEqual(day12.day12('day12t.txt', 1), 31)

    def test_day12b_1(self):
        self.assertEqual(day12.day12('day12t.txt', 1), day12b.day12('day12t.txt', 1))

    def test_day12_2(self):
        self.assertEqual(day12.day12('day12t.txt', 2), 29)

    def test_day12b_2(self):
        self.assertEqual(day12.day12('day12t.txt', 2), day12b.day12('day12t.txt', 2))

class TestDay13(unittest.TestCase):

    def test_check_ints_lt(self):
        self.assertEqual(day13.check_order(5, 10), -1)

    def test_check_ints_gt(self):
        self.assertEqual(day13.check_order(15, 10), 1)

    def test_check_ints_lt(self):
        self.assertEqual(day13.check_order(10, 10), 0)

    def test_check_lists_lt(self):
        self.assertEqual(day13.check_order([1,1], [1,2]), -1)

    def test_check_lists_gt(self):
        self.assertEqual(day13.check_order([1,1, 3], [1,1,2]), 1)

    def test_check_lists_lt2(self):
        self.assertEqual(day13.check_order([1], [1,2]), -1)

    def test_check_lists_gt(self):
        self.assertEqual(day13.check_order([1,1, 3], [1,1]), 1)

    def test_check_lists_complex1(self):
        self.assertEqual(day13.check_order([1,[1, 2, [3]], 3], [1,[1, 2, 3], 4]), -1)

    def test_check_lists_complex2(self):
        self.assertEqual(day13.check_order([1,[1, 2, [3]], [5]], [1,[1, 2, 3], 4]), 1)

    def test_day13_1(self):
        self.assertEqual(day13.day13_1('day13t.txt'), 13)

    def test_day13_2(self):
        self.assertEqual(day13.day13_2('day13t.txt'), 140)

class TestDay14(unittest.TestCase):

    def test_day14_1(self):
        self.assertEqual(day14.day14('day14t.txt'), 24)

    def test_day14_1p(self):
        self.assertEqual(day14.day14('day14.txt'), 618)

    def test_day14_2(self):
        self.assertEqual(day14.day14('day14t.txt', 2), 93)

class TestDay15(unittest.TestCase):

    def test_day15_1(self):
        self.assertEqual(day15.day15_1('day15t.txt', 10), 26)

    def test_day15_2(self):
        self.assertEqual(day15.day15_2('day15t.txt', 20), 56000011)

class TestDay16(unittest.TestCase):

    def test_day16_1(self):
        self.assertEqual(day16.day16('day16t.txt'), 1651)

    def test_day16_2(self):
        self.assertEqual(day16.day16('day16t.txt', 2), 1707)

class TestDay17(unittest.TestCase):

    def test_day17_1(self):
        self.assertEqual(day17.day17('day17t.txt', 2022), 3068)

    def test_day17_2(self):
        self.assertEqual(day17.day17('day17t.txt', 1000000000000), 1514285714288)

class TestDay18(unittest.TestCase):

    def test_day18_1(self):
        self.assertEqual(day18.day18('day18t.txt'), 64)

    def test_day18_2(self):
        self.assertEqual(day18.day18('day18t.txt', True), 58)

class TestDay19(unittest.TestCase):

    def test_day19_1a(self):
        self.assertEqual(day19.day19_1('day19t.txt'), 33)

    # def test_day19_1b(self):
        # self.assertEqual(day19.day19_1('day19.txt'), 2160)

    def test_day19_2(self):
        self.assertEqual(day19.day19_2('day19t.txt'), 56 * 62)

if __name__ == '__main__':
    unittest.main()