from day_4_passport_scanner.passport_scanner import is_passport_valid


class TestIsPassportValid:
    def test_when_passport_is_valid(self):
        # given
        passport = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm
        """

        # then
        assert is_passport_valid(passport)


    def test_when_passport_is_invalid_when_byr_is_missing(self):
        # given
        passport = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
iyr:2017 cid:147 hgt:183cm
        """

        # then
        assert is_passport_valid(passport) is False

    def test_when_passport_is_invalid_when_iyr_is_missing(self):
        # given
        passport = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 cid:147 hgt:183cm
        """

        # then
        assert is_passport_valid(passport) is False

    def test_when_passport_is_invalid_when_eyr_is_missing(self):
        # given
        passport = """
ecl:gry pid:860033327 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm
        """

        # then
        assert is_passport_valid(passport) is False


    def test_when_passport_is_invalid_when_hgt_is_missing(self):
        # given
        passport = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147
        """

        # then
        assert is_passport_valid(passport) is False

    def test_when_passport_is_invalid_when_hcl_is_missing(self):
        # given
        passport = """
ecl:gry pid:860033327 eyr:2020
byr:1937 iyr:2017 cid:147 hgt:183cm
        """

        # then
        assert is_passport_valid(passport) is False


    def test_when_passport_is_invalid_when_ecl_is_missing(self):
        # given
        passport = """
pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm
        """

        # then
        assert is_passport_valid(passport) is False

    def test_when_passport_is_invalid_when_pid_is_missing(self):
        # given
        passport = """
ecl:gry eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm
        """

        # then
        assert is_passport_valid(passport) is False

    def test_when_passport_is_valid_when_cid_is_missing(self):
        # given
        passport = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 hgt:183cm
        """

        # then
        assert is_passport_valid(passport)


    def test_is_valid_when_passport_is_from_north_pole_but_containing_every_required_field(self):
        # given
        passport = """
hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm
        """

        # then
        assert is_passport_valid(passport) is True
