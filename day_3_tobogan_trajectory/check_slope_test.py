from day_3_tobogan_trajectory.check_slope import count_trees_on_the_slope
from day_3_tobogan_trajectory.map import Map


class TestCheckSlock:
    def test_should_count_no_tree_on_the_slope(self):
        # given
        map = Map(pattern=[
            '..',
            '..'
        ])

        # when
        assert count_trees_on_the_slope(map) == 0

    def test_should_count_one_tree_on_the_slope(self):
        # given
        map = Map(pattern=[
            '....',
            '...#'
        ])

        # when
        assert count_trees_on_the_slope(map) == 1

    def test_should_count_1_tree_on_the_slope_with_example(self):
        # given
        map = Map(pattern=[
            '..##.......',
            '#...#...#..',
            '.#....#..#.',
        ])

        # when
        assert count_trees_on_the_slope(map) == 1

    def test_should_count_2_tree_on_the_slope_with_example(self):
        # given
        map = Map(pattern=[
            '..##.......',
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.'
        ])

        # when
        assert count_trees_on_the_slope(map) == 2

    def test_should_count_7_tree_on_the_slope_with_full_example(self):
        # given
        map = Map(pattern=[
            '..##.......',
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.',
            '..#.##.....',
            '.#.#.#....#',
            '.#........#',
            '#.##...#...',
            '#...##....#',
            '.#..#...#.#',
        ])

        # when
        assert count_trees_on_the_slope(map) == 7
