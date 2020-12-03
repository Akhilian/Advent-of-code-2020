from day_2_tobogan.password_validator import OldPolicy, \
    count_valid_password


class TestCountValidPasswords:
    def test_count_no_valid_passwords(self):
        # when
        result = count_valid_password([(OldPolicy(minimum_occurences=1, max_occurences=1, letter_checked='a'), 'b')])

        # then
        assert result == 0

    def test_count_1_valid_passwords(self):
        # when
        result = count_valid_password([(OldPolicy(minimum_occurences=1, max_occurences=1, letter_checked='a'), 'a')])

        # then
        assert result == 1

    def test_count_1_valid_and_1_wrong_passwords(self):
        # when
        result = count_valid_password([
            (OldPolicy(minimum_occurences=1, max_occurences=1, letter_checked='a'), 'a'),
            (OldPolicy(minimum_occurences=1, max_occurences=1, letter_checked='a'), 'b')
        ])

        # then
        assert result == 1
