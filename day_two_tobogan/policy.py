from typing import List, \
    Tuple, \
    Any

from common.file_reader import FileReader
from day_two_tobogan.password_validator import count_valid_password


class Policy():
    def __init__(self, first_position: int, second_position: int, letter_checked: str):
        self.first_position = first_position
        self.second_position = second_position
        self.letter_checked = letter_checked

    def is_password_valid(self, password) -> True:
        password_letters = list(password)
        is_first_position_match_letter = password_letters[self.first_position - 1] == self.letter_checked
        is_second_position_match_letter = password_letters[self.second_position - 1] == self.letter_checked

        if is_first_position_match_letter and is_second_position_match_letter:
            return False

        if is_first_position_match_letter or is_second_position_match_letter:
            return True

        return False

    @staticmethod
    def parse_registry(registry: str) -> ('Policy', str):
        [raw_policy, password] = registry.split(':')
        [occurences, letter] = raw_policy.split()
        [first, second] = occurences.split('-')
        return Policy(letter_checked=letter, first_position=int(first), second_position=int(second)), password.strip()


if __name__ == '__main__':
    if __name__ == '__main__':
        file_reader = FileReader('./input')
        password_registry = file_reader.to_str_list()
        parsed_registry = [Policy.parse_registry(line) for line in password_registry]

        print(count_valid_password(parsed_registry))

