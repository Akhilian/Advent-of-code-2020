from day_5_boarding_pass.boarding_pass import BoardingPass, \
    find_missing_boarding_pass


class TestColumn:
    def test_should_be_column_5_with_full_sequence(self):
        # given
        boarding_pass = BoardingPass('FBFBBFFRLR')

        # then
        assert boarding_pass.get_column() == 5

    def test_should_be_column_7_with_full_sequence(self):
        # given
        boarding_pass = BoardingPass('BFFFBBFRRR')

        # then
        assert boarding_pass.get_column() == 7

    def test_should_be_column_0_with_full_sequence(self):
        # given
        boarding_pass = BoardingPass('BFFFBBFLLL')

        # then
        assert boarding_pass.get_column() == 0


class TestGetRows:
    def test_when_starting_with_F_should_be_in_the_front(self):
        # given
        boarding_pass = BoardingPass('F')

        # then
        assert boarding_pass.get_row() <= 63

    def test_when_starting_with_B_should_be_in_the_back(self):
        # given
        boarding_pass = BoardingPass('B')

        # then
        assert boarding_pass.get_row() > 63

    def test_when_in_front_B_means_upper_half(self):
        # given
        boarding_pass = BoardingPass('FB')

        # then
        row = boarding_pass.get_row()
        assert row <= 63
        assert row >= 32

    def test_when_in_lowerfront_F_means_lower_half(self):
        # given
        boarding_pass = BoardingPass('FBF')

        # then
        row = boarding_pass.get_row()
        assert row <= 47
        assert row >= 32

    def test_when_in_another_B_means_lower_half(self):
        # given
        boarding_pass = BoardingPass('FBFB')

        # then
        row = boarding_pass.get_row()
        assert row <= 47
        assert row >= 40


class TestBoardingPass:
    def test_should_be_raw_44_with_full_sequence(self):
        # given
        boarding_pass = BoardingPass('FBFBBFFRLR')

        # then
        assert boarding_pass.get_row() == 44
        assert boarding_pass.get_column() == 5
        assert boarding_pass.get_seat_id() == 357

    def test_should_be_raw_70_with_full_sequence(self):
        # given
        boarding_pass = BoardingPass('BFFFBBFRRR')

        # then
        assert boarding_pass.get_row() == 70
        assert boarding_pass.get_column() == 7
        assert boarding_pass.get_seat_id() == 567

    def test_should_be_raw_14_with_full_sequence(self):
        # given
        boarding_pass = BoardingPass('FFFBBBFRRR')

        # then
        assert boarding_pass.get_row() == 14
        assert boarding_pass.get_column() == 7
        assert boarding_pass.get_seat_id() == 119

    def test_should_be_raw_102_with_full_sequence(self):
        # given
        boarding_pass = BoardingPass('BBFFBBFRLL')

        # then
        assert boarding_pass.get_row() == 102
        assert boarding_pass.get_column() == 4
        assert boarding_pass.get_seat_id() == 820


class TestIsBoardingPassMissing:
    def test_is_2_when_surrounding_seats_id_are_there(self):
        # given
        seats = [1, 3]

        # than
        assert find_missing_boarding_pass(seats) == 2
