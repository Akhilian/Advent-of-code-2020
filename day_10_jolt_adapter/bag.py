from functools import wraps
from time import time
from typing import List, \
    Tuple

from common.file_reader import FileReader


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r took: %2.4f sec' % (f.__name__, te-ts))
        return result
    return wrap

class Bag:
    def __init__(self, adapters: List[int]):
        self.rating = max(adapters) + 3
        self._adapters = adapters

    def find_chains(self) -> List[int]:
        return sorted(self._adapters)

    def count_jolt_differences(self, difference: int) -> int:
        adapters = self.find_chains()
        tuples = self._iterate_by_pairs(adapters)

        count = 1
        for (adapter1, adapter2) in tuples:
            if adapter2 - adapter1 == difference:
                count += 1

        return count

    def _iterate_by_pairs(self, list) -> List[Tuple]:
        max_index = len(list)
        tuples = []
        for index, item in enumerate(list):
            if index + 1 < max_index:
                tuples.append((item, list[index + 1]))
        return tuples

    @timing
    def count_possible_ways(self):
        adapters = self.find_chains()
        possibles_ways = [
            [0]
        ]

        for index, adapter in enumerate(adapters):
            possibles_ways = [way for way in possibles_ways if not (way[-1] + 3 < adapter)]

            compatible_ways = [way for way in possibles_ways if adapter > way[-1] and adapter - way[-1] <= 3]
            for compatible_way in compatible_ways:
                possibles_ways.append(compatible_way.copy())
                compatible_way.append(adapter)

        return len([way for way in possibles_ways if way[-1] == max(adapters)])


if __name__ == '__main__':
    file_reader = FileReader('./input.txt')
    adapters = file_reader.to_int_list()

    bag = Bag(adapters)
    print(f"⚡️ Counting adapters with 1 difference : {bag.count_jolt_differences(1)}")
    print(f"⚡️ Counting adapters with 3 difference : {bag.count_jolt_differences(3)}")

    print(f"Multiplied : {bag.count_jolt_differences(1) * bag.count_jolt_differences(3)}")

    print(f"Possible ways : {bag.count_possible_ways()}")
