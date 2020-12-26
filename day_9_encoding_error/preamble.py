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


def find_contiguous_numbers(sequence: List[int], value: int) -> List[int]:
    for start_index, v in enumerate(sequence):
        end_index = start_index

        value_is_reached_or_passed = False
        while not value_is_reached_or_passed:
            end_index += 1
            subsequence = sequence[start_index:end_index]

            total = sum(subsequence)

            if total >= value:
                value_is_reached_or_passed = True

        if total == value:
            return subsequence

if __name__ == '__main__':
    file_reader = FileReader('./input')
    instructions = file_reader.to_int_list()

    invalid_key = find_weak_sequence(instructions, 25)
    print(f"Invalid Code 🔑 : {invalid_key}")
    min = min(find_contiguous_numbers(instructions, invalid_key))
    max = max(find_contiguous_numbers(instructions, invalid_key))
    print(f"Min value ➖ : {min}")
    print(f"Max value ➕ : {max}")
    print(f"Total 🧮 : {min + max}")
