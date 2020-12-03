from common.file_reader import FileReader
from day_3_tobogan_trajectory.map import Map


def count_trees_on_the_slope(map: Map) -> int:
    position_down = 0
    position_right = 0
    counted_trees = 0

    while True:
        if map.is_end_of_slope_reached(position_down):
            break

        position_down = position_down + 1
        position_right = position_right + 3

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
    print(count_trees_on_the_slope(map))
