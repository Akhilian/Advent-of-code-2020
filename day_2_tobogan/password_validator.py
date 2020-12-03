from typing import List, \
    Tuple

from common.file_reader import FileReader
from day_2_tobogan.old_policy import OldPolicy


def count_valid_password(registry: List[Tuple[OldPolicy, str]]) -> int:
    return [line[0].is_password_valid(line[1]) for line in registry].count(True)


if __name__ == '__main__':
    file_reader = FileReader('./input')
    password_registry = file_reader.to_str_list()
    parsed_registry = [parse_registry(line) for line in password_registry]

    print(count_valid_password(parsed_registry))
