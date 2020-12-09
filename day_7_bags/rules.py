import re
from typing import List, \
    Union, \
    Set

from common.file_reader import FileReader


def _find(color: str, in_bag: Union[str, None], rules: dict, path: List[str] = []) -> Union[int, Set]:
    if in_bag is None:
        total = set()
        for bag_option in set(rules):
            path_new = path + [bag_option]
            find = _find(color=color, in_bag=bag_option, path=path_new, rules=rules)
            total = total.union(find)

        return len(total)

    if in_bag in rules:
        direct_colors = set(rules[in_bag])

        if len(direct_colors):
            total = set()
            for bag_option in direct_colors:
                path_new = path + [bag_option]
                result = _find(color=color, in_bag=bag_option, path=path_new, rules=rules)
                total = total.union(result)

            return total
        else:
            if color in path:
                return set(path[0:path.index(color)])
            else:
                return set()
    else:
        if color in path:
            return set(path[0:path.index(color)])
        else:
            return set()


def count_bags_options(my_color: str, rules: List[str]) -> int:
    parsed_rules = parse_rules(rules)

    return _find(color=my_color, in_bag=None, rules=parsed_rules)


def parse_rules(rules: List[str]) -> dict:
    parsed_rules = {}

    for rule in rules:
        bags_under_condition, rules_for_bag = _parse_rule(rule)
        parsed_rules[bags_under_condition] = rules_for_bag

    return parsed_rules


def _parse_rule(rule) -> (str, dict):
    bag_color_regex = '[a-zA-Z]+ [a-zA-Z]+'
    bags_under_condition = re.search(f"({bag_color_regex})", rule).group(1)
    no_rules_for_bag = re.search('contain no other bags.$', rule)
    rules_for_bag = {}
    if no_rules_for_bag:
        pass
    else:
        bag_rules = re.findall(f"([0-9]) ({bag_color_regex})", rule)
        for bag_rule in bag_rules:
            quantity = int(bag_rule[0])
            color = bag_rule[1]
            rules_for_bag[color] = quantity

    return bags_under_condition, rules_for_bag


if __name__ == '__main__':
    file_reader = FileReader('./input')
    rules = file_reader.to_str_list()
    print(rules)

    print(f"Nombre de sacs possibles 💼 - {count_bags_options('shiny gold', rules)}")
