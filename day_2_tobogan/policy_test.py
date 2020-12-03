import pytest

from day_2_tobogan.policy import Policy


class TestPasswordValidationPolicy:
    def test_password_is_valid_with_two_positions_matching_letter(self):
        # Given
        policy = Policy(first_position=1, second_position=2, letter_checked='a')
        password = 'aa'

        # then
        assert policy.is_password_valid(password) is False

    def test_password_is_valid_with_two_separated_letters(self):
        # Given
        policy = Policy(first_position=1, second_position=3, letter_checked='a')
        password = 'aba'

        # then
        assert policy.is_password_valid(password) is False

    def test_password_is_wrong_with_second_position_wrong(self):
        # Given
        policy = Policy(first_position=1, second_position=2, letter_checked='a')
        password = 'aa'

        # then
        assert policy.is_password_valid(password) is False

    def test_password_is_valid_when_first_position_match_letter_but_not_the_second_position(self):
        # Given
        policy = Policy(first_position=1, second_position=2, letter_checked='a')
        password = 'ab'

        # then
        assert policy.is_password_valid(password) is True

    def test_password_is_wrong_when_none_position_matches_the_letter(self):
        # Given
        policy = Policy(first_position=1, second_position=2, letter_checked='a')
        password = 'cd'

        # then
        assert policy.is_password_valid(password) is False

    @pytest.mark.parametrize("policy,password,is_valid", [
        (Policy(first_position=1, second_position=3, letter_checked='a'), "abcde", True),
        (Policy(first_position=1, second_position=3, letter_checked='b'), "cdefg", False),
        (Policy(first_position=2, second_position=9, letter_checked='c'), "ccccccccc", False)]
                             )
    def test_password_is_matching_examples(self, password, policy, is_valid):
        # then
        assert policy.is_password_valid(password) is is_valid

    class TestParseRegistry:
        def test_return_a_policy_and_a_password(self):
            # given
            registry = '1-9 x: xwjgxtmrzxzmkx'

            # when
            (policy, password) = Policy.parse_registry(registry)

            # then
            assert password == 'xwjgxtmrzxzmkx'
            assert isinstance(policy, Policy)
            assert policy.letter_checked == 'x'
            assert policy.first_position == 1
            assert policy.second_position == 9
