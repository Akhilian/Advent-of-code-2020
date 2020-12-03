import pytest

from day_two_tobogan.password_validator import OldPolicy, \
    count_valid_password


class TestPasswordValidator:
    def test_password_is_valid_with_one_letter_expected(self):
        # Given
        policy = OldPolicy(minimum_occurences=1, max_occurences=1, letter_checked='a')
        password = 'a'

        # then
        assert policy.is_password_valid(password)

    def test_password_is_invalid_when_expected_letter_is_not_found(self):
        # Given
        policy = OldPolicy(minimum_occurences=1, max_occurences=1, letter_checked='a')
        password = 'b'

        # then
        assert policy.is_password_valid(password) is False

    def test_password_is_invalid_when_letter_is_found_to_few_times(self):
        # Given
        policy = OldPolicy(minimum_occurences=2, max_occurences=2, letter_checked='a')
        password = 'ab'

        # then
        assert policy.is_password_valid(password) is False

    def test_password_is_invalid_when_letter_is_found_to_many_times(self):
        # Given
        policy = OldPolicy(minimum_occurences=1, max_occurences=2, letter_checked='a')
        password = 'aaa'

        # then
        assert policy.is_password_valid(password) is False

    @pytest.mark.parametrize("policy,password,is_valid", [
        (OldPolicy(minimum_occurences=1, max_occurences=3, letter_checked='a'), "abcde", True),
        (OldPolicy(minimum_occurences=1, max_occurences=3, letter_checked='b'), "cdefg", False),
        (OldPolicy(minimum_occurences=2, max_occurences=9, letter_checked='c'), "ccccccccc", True)]
                             )
    def test_password_is_matching_examples(self, password, policy, is_valid):
        # then
        assert policy.is_password_valid(password) is is_valid


class TestParseRegistry:
    def test_return_a_policy_and_a_password(self):
        # given
        registry = '1-9 x: xwjgxtmrzxzmkx'

        # when
        (policy, password) = OldPolicy.parse_registry(registry)

        # then
        assert password == 'xwjgxtmrzxzmkx'
        assert isinstance(policy, OldPolicy)
        assert policy.letter_checked == 'x'
        assert policy.minimum_occurences == 1
        assert policy.max_occurences == 9
