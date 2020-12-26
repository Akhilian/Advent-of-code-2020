from day_9_encoding_error.preamble import is_valid, \
    find_weak_sequence, \
    find_contiguous_numbers

preamble = list(range(1, 26))


class TestPreamble:
    def test_is_valid_when_value_is_26(self):
        assert is_valid(preamble, 26)

    def test_is_valid_when_value_is_49(self):
        assert is_valid(preamble, 49)

    def test_is_invalid_when_value_is_100(self):
        assert not is_valid(preamble, 100)

    def test_is_invalid_when_value_is_50(self):
        assert not is_valid(preamble, 50)


class TestSequence:
    def test_is_valid_sequence_should_check_last_item(self):
        # given
        sequence = [20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 45]

        assert find_weak_sequence(sequence, 25) is None

    def test_26_is_valid_in_sequence(self):
        # given
        sequence = [20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 45, 26]

        assert find_weak_sequence(sequence, 25) is None

    def test_65_is_not_valid_in_sequence_cause_20_is_ignored(self):
        # given
        sequence = [20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 45, 65]

        assert find_weak_sequence(sequence, 25) == 65

    def test_64_is_valid_in_sequence_cause_19_and_45_adds_up(self):
        # given
        sequence = [20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 45, 64]

        assert find_weak_sequence(sequence, 25) is None

    def test_66_is_valid_in_sequence_cause_21_and_45_adds_up(self):
        # given
        sequence = [20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 45, 64]

        assert find_weak_sequence(sequence, 25) is None

    def test_works_with_a_shorted_preamble_size(self):
        # given
        sequence = [
            35,
            20,
            15,
            25,
            47,
            40
        ]

        assert find_weak_sequence(sequence, 5) is None

    def test_using_example_values(self):
        # given
        sequence = [
            35,
            20,
            15,
            25,
            47,
            40,
            62,
            55,
            65,
            95,
            102,
            117,
            150,
            182,
            127,
            219,
            299,
            277,
            309,
            576
        ]

        assert find_weak_sequence(sequence, 5) == 127


class TestFindContiguousNumbers:
    def test_find_closed_numbers_that_sums_to_given_value(self):
        # given
        preamble = [1, 2, 3]

        # when
        result = find_contiguous_numbers(preamble, 3)

        # then
        assert result == [1, 2]

    def test_find_closed_numbers_with_the_example(self):
        # given
        preamble = [
            35,
            20,
            15,
            25,
            47,
            40,
            62,
            55,
            65,
            95,
            102,
            117,
            150,
            182,
            127,
            219,
            299,
            277,
            309,
            576
        ]

        # when
        result = find_contiguous_numbers(preamble, 127)

        # then
        assert result == [15, 25, 47, 40]
