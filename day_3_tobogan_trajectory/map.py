from typing import List


class Map():
    def __init__(self, pattern : List[str]):
        self.pattern = pattern
        self._transformed_pattern = [list(down) for down in self.pattern]
        self._dimensions = { "right": len(self._transformed_pattern[0]), "down": len(self._transformed_pattern) }

    def check_position(self, right: int, down: int) -> str:
        if right >= self._dimensions.get('right'):
            right = right % self._dimensions.get('right')

        return self._transformed_pattern[down][right]

    def is_end_of_slope_reached(self, down: int) -> bool:
        return down + 1 >= self._dimensions.get('down')
