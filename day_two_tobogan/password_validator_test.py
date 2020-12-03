import pytest

from day_two_tobogan.password_validator import is_password_valid, \
    Policy, \
    parse_registry, \
    count_valid_password
import pytest

from day_two_tobogan.password_validator import is_password_valid, \
    Policy


class TestPasswordValidator:
    def test_password_is_valid_with_one_letter_expected(self):
        # Given
        policy = Policy(minimum_occurences=1, max_occurences=1, letter_checked='a')
        password = 'a'

        # then
        assert is_password_valid(policy, password)

    def test_password_is_invalid_when_expected_letter_is_not_found(self):
        # Given
        policy = Policy(minimum_occurences=1, max_occurences=1, letter_checked='a')
        password = 'b'

        # then
        assert is_password_valid(policy, password) is False

    def test_password_is_invalid_when_letter_is_found_to_few_times(self):
        # Given
        policy = Policy(minimum_occurences=2, max_occurences=2, letter_checked='a')
        password = 'ab'

        # then
        assert is_password_valid(policy, password) is False

    def test_password_is_invalid_when_letter_is_found_to_many_times(self):
        # Given
        policy = Policy(minimum_occurences=1, max_occurences=2, letter_checked='a')
        password = 'aaa'

        # then
        assert is_password_valid(policy, password) is False

    @pytest.mark.parametrize("policy,password,is_valid", [
        (Policy(minimum_occurences=1, max_occurences=3, letter_checked='a'), "abcde", True),
        (Policy(minimum_occurences=1, max_occurences=3, letter_checked='b'), "cdefg", False),
        (Policy(minimum_occurences=2, max_occurences=9, letter_checked='c'), "ccccccccc", True)]
                             )
    def test_password_is_matching_examples(self, password, policy, is_valid):
        # then
        assert is_password_valid(policy, password) is is_valid


class TestParseRegistry:
    def test_return_a_policy_and_a_password(self):
        # given
        registry = '1-9 x: xwjgxtmrzxzmkx'

        # when
        (policy, password) = parse_registry(registry)

        # then
        assert password == 'xwjgxtmrzxzmkx'
        assert isinstance(policy, Policy)
        assert policy.letter_checked == 'x'
        assert policy.minimum_occurences == 1
        assert policy.max_occurences == 9

class TestCountValidPasswords:
    def test_count_no_valid_passwords(self):
        # when
        result = count_valid_password([(Policy(minimum_occurences=1, max_occurences=1, letter_checked='a'), 'b')])

        # then
        assert result == 0

    def test_count_1_valid_passwords(self):
        # when
        result = count_valid_password([(Policy(minimum_occurences=1, max_occurences=1, letter_checked='a'), 'a')])

        # then
        assert result == 1

    def test_count_1_valid_and_1_wrong_passwords(self):
        # when
        result = count_valid_password([
            (Policy(minimum_occurences=1, max_occurences=1, letter_checked='a'), 'a'),
            (Policy(minimum_occurences=1, max_occurences=1, letter_checked='a'), 'b')
        ])

        # then
        assert result == 1
