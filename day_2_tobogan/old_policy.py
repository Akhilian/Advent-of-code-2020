from typing import List, \
    Tuple, \
    Any

from common.file_reader import FileReader


class OldPolicy():
    def __init__(self, minimum_occurences: int, max_occurences: int, letter_checked: str):
        self.minimum_occurences = minimum_occurences
        self.max_occurences = max_occurences
        self.letter_checked = letter_checked

    def is_password_valid(self, password) -> True:
        count = list(password).count(self.letter_checked)
        return self.minimum_occurences <= count <= self.max_occurences

    @staticmethod
    def parse_registry(registry: str) -> ('OldPolicy', str):
        [raw_policy, password] = registry.split(':')
        [occurences, letter] = raw_policy.split()
        [min, max] = occurences.split('-')
        return OldPolicy(letter_checked=letter, minimum_occurences=int(min), max_occurences=int(max)), password.strip()


def count_valid_password(registry: List[Tuple[OldPolicy, str]]) -> int:
    return [line[0].is_password_valid(line[1]) for line in registry].count(True)


if __name__ == '__main__':
    file_reader = FileReader('./input')
    password_registry = file_reader.to_str_list()
    parsed_registry = [OldPolicy.parse_registry(line) for line in password_registry]

    print(count_valid_password(parsed_registry))
