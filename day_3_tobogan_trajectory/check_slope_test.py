import pytest

from day_3_tobogan_trajectory.check_slope import count_trees_on_the_slope, \
    Trajectory
from day_3_tobogan_trajectory.map import Map


class TestCheckSlock:
    def test_should_count_no_tree_on_the_slope(self):
        # given
        trajectory = Trajectory(right=3, down=1)
        map = Map(pattern=[
            '..',
            '..'
        ])

        # when
        assert count_trees_on_the_slope(map, trajectory) == 0

    def test_should_count_one_tree_on_the_slope(self):
        # given
        trajectory = Trajectory(right=3, down=1)
        map = Map(pattern=[
            '....',
            '...#'
        ])

        # when
        assert count_trees_on_the_slope(map, trajectory) == 1

    def test_should_count_1_tree_on_the_slope_with_example(self):
        # given
        trajectory = Trajectory(right=3, down=1)
        map = Map(pattern=[
            '..##.......',
            '#...#...#..',
            '.#....#..#.',
        ])

        # when
        assert count_trees_on_the_slope(map, trajectory) == 1

    def test_should_count_2_tree_on_the_slope_with_example(self):
        # given
        trajectory = Trajectory(right=3, down=1)
        map = Map(pattern=[
            '..##.......',
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.'
        ])

        # when
        assert count_trees_on_the_slope(map, trajectory) == 2

    def test_should_count_7_tree_on_the_slope_with_full_example(self):
        # given
        trajectory = Trajectory(right=3, down=1)
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
        assert count_trees_on_the_slope(map, trajectory) == 7

    @pytest.mark.parametrize("trajectory,tree_count", [
        (Trajectory(right=1, down=1), 2),
        (Trajectory(right=3, down=1), 7),
        (Trajectory(right=5, down=1), 3),
        (Trajectory(right=7, down=1), 4),
        (Trajectory(right=1, down=2), 2)
    ])
    def test_should_count_2_tree_on_different_trajectory(self, trajectory, tree_count):
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
        assert count_trees_on_the_slope(map, trajectory) == tree_count
