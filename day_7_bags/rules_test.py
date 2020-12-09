from day_7_bags.rules import parse_rules, \
    count_bags_options


class TestRules:
    def test_should_parse_a_single_rule(self):
        # given
        rules = parse_rules(["shiny aqua bags contain 1 dark white bag."])

        # then
        assert rules == {
            "shiny aqua": {
                "dark white": 1
            }
        }

    def test_one_bag_should_contain_more_than_1_other_bag(self):
        # given
        rules = parse_rules(["shiny aqua bags contain 2 dark white bag."])

        # then
        assert rules == {
            "shiny aqua": {
                "dark white": 2
            }
        }

    def test_one_bag_should_contain_two_kinds_of_bags(self):
        # given
        rules = parse_rules(["dark orange bags contain 3 bright white bags, 4 muted yellow bags."])

        # then
        assert rules == {
            "dark orange": {
                "bright white": 3,
                "muted yellow": 4
            }
        }

    def test_one_bag_should_contain_three_kinds_of_bags(self):
        # given
        rules = parse_rules(
            ["muted blue bags contain 1 vibrant lavender bag, 4 dotted silver bags, 2 dim indigo bags."])

        # then
        assert rules == {
            "muted blue": {
                "vibrant lavender": 1,
                "dotted silver": 4,
                "dim indigo": 2
            }
        }

    def test_should_parse_a_no_other_bag_needed(self):
        # given
        rules = parse_rules(["shiny aqua bags contain no other bags."])

        # then
        assert rules == {
            "shiny aqua": {}
        }

    def test_should_work_for_multiple_lines(self):
        # given
        rules = parse_rules(["dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
                             "shiny aqua bags contain no other bags."])

        # then
        assert rules == {
            "dark orange": {
                "bright white": 3,
                "muted yellow": 4
            },
            "shiny aqua": {}
        }


class TestCountPossibleBags:
    def test_should_count_zero_when_no_rules(self):
        # given
        rules = []

        # when
        assert count_bags_options('shiny gold', rules) == 0

    def test_should_count_zero_when_bags_possibles(self):
        # given
        rules = [
            "faded blue bags contain no other bags.",
        ]

        # when
        assert count_bags_options('shiny gold', rules) == 0

    def test_should_count_one_on_simple_flat_level(self):
        # given
        rules = ["bright white bags contain 1 shiny gold bag."]

        # when
        assert count_bags_options('shiny gold', rules) == 1

    def test_should_count_a_bag_only_once(self):
        # given
        rules = [
            "bright white bags contain 1 shiny gold bag.",
            "bright white bags contain 1 shiny gold bag."
        ]

        # when
        assert count_bags_options('shiny gold', rules) == 1

    def test_should_cound_two_bags_in_a_simple_way(self):
        # given
        rules = [
            "bright white bags contain 1 shiny gold bag.",
            "muted yellow bags contain 1 shiny gold bag."
        ]

        # when
        assert count_bags_options('shiny gold', rules) == 2

    def test_should_count_two_on_simple_flat_level(self):
        # given
        rules = ["bright white bags contain 1 shiny gold bag.",
                 "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags."]

        # when
        assert count_bags_options('shiny gold', rules) == 2

    def test_should_count_one_one_multiple_levels(self):
        # given
        rules = ["bright white bags contain 1 shiny gold bag.",
                 "dark orange bags contain 3 bright white bags, 4 muted yellow bags."]

        # when
        assert count_bags_options('shiny gold', rules) == 2

    def test_should_return_0_with_simpler_example(self):
        # given
        rules = [
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
        ]

        # when
        assert count_bags_options('shiny gold', rules) == 0

    def test_should_return_4_with_full_example(self):
        # given
        rules = [
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            "bright white bags contain 1 shiny gold bag.",
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags."
        ]

        # when
        assert count_bags_options('shiny gold', rules) == 4
