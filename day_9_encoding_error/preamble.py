from typing import List

from common.file_reader import FileReader


def is_valid(preamble: List[int], value: int) -> bool:
    for key in preamble:
        missing_value = value - key

        if missing_value != key and missing_value in preamble:
            return True

    return False


def find_weak_sequence(sequence: List[int], preamble_size: int) -> int:
    for i, value in enumerate(sequence):
        observed_sequence = sequence[i:(i + preamble_size + 1)]
        value = observed_sequence.pop(-1)

        if len(observed_sequence) < preamble_size:
            return None

        if not is_valid(observed_sequence, value):
            return value

    return None


if __name__ == '__main__':
    file_reader = FileReader('./input')
    instructions = file_reader.to_int_list()

    print(f"Code : {find_weak_sequence(instructions, 25)}")
