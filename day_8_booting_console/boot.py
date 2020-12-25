from typing import List

from common.file_reader import FileReader


def run_console(instructions: List[str]):
    acc = 0
    has_fail = False
    index = 0
    count_of_instructions = len(instructions)
    read_instructions = []

    while index < count_of_instructions:
        if index in read_instructions:
            has_fail = True
            break

        instruction = instructions[index]
        (instruction, offset) = instruction.split()
        read_instructions.append(index)

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
    alternative_instructions = [instructions]
    for i, value in enumerate(instructions):
        copy = instructions.copy()

        (instruction, offset) = copy[i].split()
        if instruction == 'jmp':
            instruction = 'nop'
        elif instruction == 'nop':
            instruction = 'jmp'

        copy[i] = ' '.join([instruction, offset])

        alternative_instructions.append(copy)

    for instruction in alternative_instructions:
        execution_trace = run_console(instruction)

        if execution_trace['has_failed'] is False:
            return execution_trace



if __name__ == '__main__':
    file_reader = FileReader('./input')
    instructions = file_reader.to_str_list()

    print(f"Accumulator 🤖 - {run_console(instructions)['accumulator']}")
    print(f"Fixed accumulator 🤖 - {fix_instructions(instructions)['accumulator']}")
