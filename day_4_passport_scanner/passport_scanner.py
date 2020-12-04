from common.file_reader import FileReader


def is_passport_valid(passport: str) -> bool:
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return [field in passport for field in required_fields].count(False) == 0

if __name__ == '__main__':
    file_reader = FileReader('./input')
    passports = file_reader.to_str_list('\n\n')

    print([is_passport_valid(passport) for passport in passports].count(True))
