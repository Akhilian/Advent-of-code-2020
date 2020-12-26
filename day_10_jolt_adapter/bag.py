from typing import List, \
    Tuple

from common.file_reader import FileReader

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

if __name__ == '__main__':
    file_reader = FileReader('./input.txt')
    adapters = file_reader.to_int_list()

    bag = Bag(adapters)
    print(f"⚡️ Counting adapters with 1 difference : {bag.count_jolt_differences(1)}")
    print(f"⚡️ Counting adapters with 3 difference : {bag.count_jolt_differences(3)}")

    print(f"Multiplied : {bag.count_jolt_differences(1) * bag.count_jolt_differences(3)}")
