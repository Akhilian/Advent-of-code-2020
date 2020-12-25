from pprint import pprint
from typing import List

from common.file_reader import FileReader


def run_console(instructions: List[str]):
    print()
    acc = 0
    has_fail = False
    index = 0
    count_of_instructions = len(instructions)
    print(f"Numbre d'instruction {count_of_instructions}")
    read_instructions = []

    while index < count_of_instructions:
        if index in read_instructions:
            print(f"Breaking on {index} {instruction} {offset}")
            has_fail = True
            break
            # if instruction == 'jmp':
            #     instruction = 'nop'
            # elif instruction == 'nop':
            #     instruction = 'jmp'

        instruction = instructions[index]
        (instruction, offset) = instruction.split()
        read_instructions.append(index)
        print(f"Running {index} : {instruction} {offset}")

        if instruction == 'jmp':
            next_position = index + int(offset)
            index = next_position

        if instruction == 'nop':
            index += 1

        if instruction == 'acc':
            index += 1
            acc += int(offset)

    return {
        "accumulator": acc,
        "has_failed": has_fail
    }


def fix_instructions(instructions: List[str]):
    is_fixed = False

    alternative_instructions = []
    for i, value in enumerate(instructions):
        copy = instructions.copy()

        (instruction, offset) = copy[i].split()
        print(i)
        print(instruction)
        if instruction == 'jmp':
            instruction = 'nop'
        elif instruction == 'nop':
            instruction = 'jmp'

        copy[i] = ' '.join([instruction, offset])
        print(copy)

        alternative_instructions.append(copy)

    # for instructions in alternative_instructions:
    #     print(instructions)
    # while not is_fixed:
    #
    #     result = run_console(instructions)
    #     is_fixed = result['has_failed']

    return result



if __name__ == '__main__':
    file_reader = FileReader('./input')
    instructions = file_reader.to_str_list()

    print(f"Accumulator 🤖 - {run_console(instructions)['accumulator']}")
