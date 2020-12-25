from common.file_reader import FileReader
from day_8_booting_console.boot import run_console, \
    fix_instructions


class TestA:
    def test_accumulator_adds_up_1(self):
        # given
        instructions = [
            "acc +1"
        ]

        # when
        trace = run_console(instructions)

        # then
        assert trace["accumulator"] == 1

    def test_accumulator_adds_up_2(self):
        # given
        instructions = [
            "acc +2"
        ]

        # when
        trace = run_console(instructions)

        # then
        assert trace["accumulator"] == 2

    def test_multiple_accumulator_adds_up(self):
        # given
        instructions = [
            "acc +2",
            "acc +5"
        ]

        # when
        trace = run_console(instructions)

        # then
        assert trace["accumulator"] == 7

    def test_nope_does_not_add_anything(self):
        # given
        code = [
            "nop +0",
        ]

        # when
        trace = run_console(code)

        # then
        assert trace["accumulator"] == 0

    def test_jmp_1_goes_to_next_instruction(self):
        # given
        instructions = [
            "jmp +2",
            "acc +1",
            "acc +2",
        ]

        # when
        trace = run_console(instructions)

        # then
        assert trace["accumulator"] == 2

    def test_should_stop_on_infinity_loop(self):
        # given
        instructions = [
            "nop +0",
            "jmp +2",
            "acc +1",
            "jmp -2",
        ]

        # when
        trace = run_console(instructions)

        # then
        assert trace["has_failed"] is True

    def test_should_fix_an_infinity_loop(self):
        # given
        instructions = [
            "jmp +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6",
        ]

        # when
        run_console(instructions)

    def test_should_return_1941_for_first_exercise(self):
        # given
        file_reader = FileReader('./input')
        instructions = file_reader.to_str_list()

        # when
        accumulator = run_console(instructions)['accumulator']

        # then
        assert accumulator == 1941


class TestFixInfinityLoop:
    def test_should_work_when_no_infinite_loop(self):
        # given
        instructions = [
            "nop +0",
        ]

        # when
        trace = fix_instructions(instructions)

        # then
        assert trace["accumulator"] == 0


    def test_should_work_when_an_infinite_loop_is_started(self):
        # given
        instructions = [
            "jmp +0",
        ]

        # when
        trace = fix_instructions(instructions)

        # then
        assert trace["accumulator"] == 0

    def test_should_fix_the_infinity_loop_and_terminate_with_8(self):
        # given
        instructions = [
            "nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6",
        ]

        # when
        trace = fix_instructions(instructions)

        # then
        assert trace["accumulator"] == 8
