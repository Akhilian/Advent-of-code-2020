from day_6_custom_declaration.count_answers import count_unique_answers, \
    count_total_answers, \
    count_answers_where_everyone_says_yes, \
    count_total_answers_part_2


class TestCountUniqueAnswers:
    def test_count_only_one(self):
        # given
        answers = "b"

        # then
        assert count_unique_answers(answers) == 1

    def test_count_two_on_multiple_lines(self):
        # given
        answers = """b
        a"""

        # then
        assert count_unique_answers(answers) == 2

    def test_count_three_on_single_line(self):
        # given
        answers = """abc"""

        # then
        assert count_unique_answers(answers) == 3

    def test_count_one_on_single_line(self):
        # given
        answers = """
        a
a
a
a
        """

        # then
        assert count_unique_answers(answers) == 1


class TestCountTotalAnswers:
    def test_return_11_with_full_example(self):
        # given
        answers_by_group = [
            """abc""",
            """a
            b
            c""",
            """ab
            ac""",
            """a
            a
            a
            a""",
            """b"""
        ]

        # when
        assert count_total_answers(answers_by_group) == 11


class TestCountAnswersWhereEveryOneSaysYes:
    def test_count_only_one(self):
        # given
        answers = "b"

        # then
        assert count_answers_where_everyone_says_yes(answers) == 1


    def test_count_one_because_everyone_answered_yes_on_b(self):
        # given
        answers = """
        b
        b
        """

        # then
        assert count_answers_where_everyone_says_yes(answers) == 1

    def test_count_one_because_everyone_answered_yes_on_b_but_not_a(self):
        # given
        answers = """
        ba
        b
        """

        # then
        assert count_answers_where_everyone_says_yes(answers) == 1

    def test_count_zero_because_noone_answered_yes_to_the_same_question(self):
        # given
        answers = """
        a
        b
        c
        """

        # then
        assert count_answers_where_everyone_says_yes(answers) == 0

class TestCountTotalAnswersPart2:
    def test_return_6_with_full_example(self):
        # given
        answers_by_group = [
            """abc""",
            """a
            b
            c""",
            """ab
            ac""",
            """a
            a
            a
            a""",
            """b"""
        ]

        # when
        assert count_total_answers_part_2(answers_by_group) == 6
