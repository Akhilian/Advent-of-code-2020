from day_3_tobogan_trajectory.map import Map


class TestCheckMapPosition:
    def test_can_draw_map_from_a_pattern(self):
        # given
        pattern = [
            '.#',
            '#.'
        ]

        # when
        map = Map(pattern=pattern)

        # then
        assert map.check_position(0, 0) == '.'
        assert map.check_position(0, 1) == '#'
        assert map.check_position(1, 0) == '#'
        assert map.check_position(1, 1) == '.'

    def test_can_check_position_when_going_right(self):
        # given
        pattern = [
            '.#',
            '#.'
        ]

        # when
        map = Map(pattern=pattern)

        # then
        assert map.check_position(down=0, right=2) == '.'
        assert map.check_position(down=0, right=3) == '#'

    def test_can_check_position_when_going_down_and_right(self):
        # given
        pattern = [
            '.#',
            '#.'
        ]

        # when
        map = Map(pattern=pattern)

        # then
        assert map.check_position(down=1, right=2) == '#'

    def test_can_check_position_when_going_down_and_right_with_a_bigger_pattern(self):
        # given
        pattern = [
            '.#.',
            '.#.',
        ]

        # when
        map = Map(pattern=pattern)

        # then
        assert map.check_position(down=1, right=3) == '.'


class TestIsEndOfSlopReached:
    def test_slope_end_when_reaching_last_level(self):
        # given
        pattern = [
            '.#',
            '#.'
        ]

        # when
        map = Map(pattern=pattern)

        # then
        assert map.is_end_of_slope_reached(1) is True

    def test_slope_is_not_ended_when_starting_from_top(self):
        # given
        pattern = [
            '.#',
            '#.'
        ]

        # when
        map = Map(pattern=pattern)

        # then
        assert map.is_end_of_slope_reached(0) is False

    def test_slope_is_not_ended_when_reaching_another_level(self):
        # given
        pattern = [
            '.#',
            '#.',
            '#.'
        ]

        # when
        map = Map(pattern=pattern)

        # then
        assert map.is_end_of_slope_reached(1) is False
