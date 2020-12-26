from day_10_jolt_adapter.bag import Bag


def test_device_is_rated_3_jots_higher_than_the_highest_in_the_bag():
    # given
    adapters = [1, 3, 2]

    # when
    bag = Bag(adapters)

    # then
    assert bag.rating == 6


class TestRatingWithTheExample:
    def test_should_have_a_rating_of_22(self):
        # given
        adapters = [
            16,
            10,
            15,
            5,
            1,
            11,
            7,
            19,
            6,
            12,
            4
        ]

        # when
        bag = Bag(adapters)

        # then
        assert bag.rating == 22


class TestFindAdaptersChain:
    def test_should_build_chains_only_that_increases_by_1_to_3_maximum_so_4_does_not_work(self):
        # given
        adapters = [
            1, 4
        ]

        # when
        bag = Bag(adapters)

        # then
        assert bag.find_chains() == [1, 4]

    def test_should_sort_all_adapters_so_they_can_chain(self):
        # given
        adapters = [
            16,
            10,
            15,
            5,
            1,
            11,
            7,
            19,
            6,
            12,
            4
        ]

        # when
        bag = Bag(adapters)

        # then
        assert bag.find_chains() == [
            1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19
        ]

def test_should_sort_all_adapters_so_they_can_chain():
    # given
    adapters = [
        16,
        10,
        15,
        5,
        1,
        11,
        7,
        19,
        6,
        12,
        4
    ]

    # when
    bag = Bag(adapters)

    # then
    assert bag.count_jolt_differences(1) == 7
    assert bag.count_jolt_differences(3) == 5


def test_should_count_jolt_difference():
    # given
    adapters = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]

    # when
    bag = Bag(adapters)

    # then
    assert bag.count_jolt_differences(1) == 22
    assert bag.count_jolt_differences(3) == 10


