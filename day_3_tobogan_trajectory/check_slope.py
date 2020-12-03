from common.file_reader import FileReader
from day_3_tobogan_trajectory.map import Map

class Trajectory:
    def __init__(self, right: int, down: int):
        self.right = right
        self.down = down


def count_trees_on_the_slope(map: Map, trajectory: Trajectory) -> int:
    position_down = 0
    position_right = 0
    counted_trees = 0

    while True:
        if map.is_end_of_slope_reached(position_down):
            break

        position_down = position_down + trajectory.down
        position_right = position_right + trajectory.right

        next_element = map.check_position(
            down=position_down, right=position_right
        )

        if next_element == '#':
            counted_trees = counted_trees + 1

    return counted_trees

if __name__ == '__main__':
    file_reader = FileReader('./input')
    slope_plan = file_reader.to_str_list()
    map = Map(pattern=slope_plan)

    slope_1 = Trajectory(right=1, down=1)
    slope_2 = Trajectory(right=3, down=1)
    slope_3 = Trajectory(right=5, down=1)
    slope_4 = Trajectory(right=7, down=1)
    slope_5 = Trajectory(right=1, down=2)

    print('Exercise 1')
    print(count_trees_on_the_slope(map, slope_2))

    print('Exercise 2')
    print(count_trees_on_the_slope(map, slope_1))
    print(count_trees_on_the_slope(map, slope_2))
    print(count_trees_on_the_slope(map, slope_3))
    print(count_trees_on_the_slope(map, slope_4))
    print(count_trees_on_the_slope(map, slope_5))

    total = count_trees_on_the_slope(map, slope_1) * count_trees_on_the_slope(map, slope_2) * count_trees_on_the_slope(map, slope_3) * count_trees_on_the_slope(map, slope_4) * count_trees_on_the_slope(map, slope_5)
    print(f"Total : {total}")
