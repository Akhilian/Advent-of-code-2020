from typing import List


class FileReader():
    def __init__(self, path: str):
        self.file = open(path, 'r')

    def to_int_list(self) -> List[int]:
        return [int(row) for row in self.file.readlines()]

    def to_str_list(self, separator: str = None) -> List[str]:
        if separator:
            return self.file.read().split(separator)
        else:
            return self.file.read().splitlines()
