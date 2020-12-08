import re
from functools import reduce

from typing import List

from common.file_reader import FileReader


def _is_outdated(field: str, min: int, max: int):
    return int(field) < min or int(field) > max


def _parse_to_dict(acc: dict, data: List[str]) -> str:
    acc[data[0]] = data[1]
    return acc


def is_passport_valid(passport: str) -> bool:
    field_definition = {
        'byr': None,
        'iyr': None,
        'eyr': None,
        'hgt': None,
        'hcl': None,
        'ecl': None,
        'pid': None,
    }

    required_fields = set(field_definition)
    is_all_fields_present = [field in passport for field in required_fields].count(False) == 0

    if not is_all_fields_present:
        return False

    split = [field.split(':') for field in passport.split()]
    fields = reduce(_parse_to_dict, split, {})

    if fields['byr']:
        if _is_outdated(fields['byr'], 1920, 2002):
            return False

    if fields['iyr']:
        if _is_outdated(fields['iyr'], 2010, 2020):
            return False

    if fields['eyr']:
        if _is_outdated(fields['eyr'], 2020, 2030):
            return False

    if fields['hgt']:
        height_and_unit = re.search('(\d+)(in|cm)', fields['hgt'])

        if not height_and_unit:
            return False

        height = int(height_and_unit.group(1))
        unit = height_and_unit.group(2)

        if unit == 'in':
            if height > 76 or height <= 59:
                return False

        if unit == 'cm':
            if height < 150 or height > 193:
                return False

    if fields['hcl']:
        if not re.match('#[\da-f]{6}', fields['hcl']):
            return False

    if fields['ecl']:
        authorized_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if fields['ecl'] not in authorized_colors:
            return False

    if fields['pid']:
        if not re.match('^\d{9}$', fields['pid']):
            return False

    return True


if __name__ == '__main__':
    file_reader = FileReader('./input')
    passports = file_reader.to_str_list('\n\n')

    print([is_passport_valid(passport) for passport in passports].count(True))
