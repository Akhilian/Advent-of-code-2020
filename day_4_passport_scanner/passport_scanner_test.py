import pytest

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

    @pytest.mark.parametrize("passport", [
        ("""
        eyr:1972 cid:100
        hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
        """),
        ("""
        iyr:2019
        hcl:#602927 eyr:1967 hgt:170cm
        ecl:grn pid:012533040 byr:1946
        """),
        ("""
        hcl:dab227 iyr:2012
        ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
        """),
    ])
    def test_passport_is_invalid_with_given_example(self, passport):
        assert is_passport_valid(passport) is False

    @pytest.mark.parametrize("passport", [
        ("""
eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
        """),
        ("""
hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022
        """),
        ("""
iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
        """)
    ])
    def test_passport_is_valid_with_given_example(self, passport):
        assert is_passport_valid(passport) is True


class TestByr:
    def test_when_passport_is_invalid_when_byr_is_missing(self):
        # given
        passport = """
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    iyr:2017 cid:147 hgt:183cm
            """

        # then
        assert is_passport_valid(passport) is False

    def test_when_passport_a_valid_birthdate(self):
        # given
        passport = """
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    iyr:2017 cid:147 hgt:183cm byr:2002
            """

        # then
        assert is_passport_valid(passport) is True

    def test_when_people_is_too_young(self):
        # given
        passport = """
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    iyr:2017 cid:147 hgt:183cm byr:2003
            """

        # then
        assert is_passport_valid(passport) is False

    def test_when_people_is_too_old(self):
        # given
        passport = """
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    iyr:2017 cid:147 hgt:183cm byr:1919
            """

        # then
        assert is_passport_valid(passport) is False


class TestIyr:
    def test_when_passport_is_invalid_when_iyr_is_missing(self):
        # given
        passport = """
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 cid:147 hgt:183cm
            """

        # then
        assert is_passport_valid(passport) is False

    def test_when_passport_a_valid_birthdate(self):
        # given
        passport = """
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    iyr:2010 cid:147 hgt:183cm byr:2001
            """

        # then
        assert is_passport_valid(passport) is True

    def test_when_passport_is_too_old(self):
        # given
        passport = """
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    iyr:2009 cid:147 hgt:183cm byr:2001
            """

        # then
        assert is_passport_valid(passport) is False

    def test_when_passport_is_too_young(self):
        # given
        passport = """
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    iyr:2021 cid:147 hgt:183cm byr:2001
            """

        # then
        assert is_passport_valid(passport) is False


class TestEyr:
    def test_when_passport_is_invalid_when_eyr_is_missing(self):
        # given
        passport = """
ecl:gry pid:860033327 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm
        """

        # then
        assert is_passport_valid(passport) is False

    def test_when_passport_is_invalid_when_eyr_is_valid(self):
        # given
        passport = """
ecl:gry pid:860033327 hcl:#fffffd eyr:2021
byr:1937 iyr:2017 cid:147 hgt:183cm
        """

        # then
        assert is_passport_valid(passport) is True

    def test_when_passport_is_expired(self):
        # given
        passport = """
ecl:gry pid:860033327 hcl:#fffffd eyr:2019
byr:1937 iyr:2017 cid:147 hgt:183cm
        """

        # then
        assert is_passport_valid(passport) is False

    def test_when_passport_is_expiring_to_late(self):
        # given
        passport = """
ecl:gry pid:860033327 hcl:#fffffd eyr:2031
byr:1937 iyr:2017 cid:147 hgt:183cm
        """

        # then
        assert is_passport_valid(passport) is False


class TestHgt:
    def test_74in_is_valid_height(self):
        # given
        passport = """
        pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
        hcl:#623a2f
        """

        # then
        assert is_passport_valid(passport)

    def test_77in_is_invalid_height(self):
        # given
        passport = """
        pid:087499704 hgt:77in ecl:grn iyr:2012 eyr:2030 byr:1980
        hcl:#623a2f
        """

        # then
        assert is_passport_valid(passport) is False

    def test_58in_is_invalid_height(self):
        # given
        passport = """
        pid:087499704 hgt:58in ecl:grn iyr:2012 eyr:2030 byr:1980
        hcl:#623a2f
        """

        # then
        assert is_passport_valid(passport) is False

    def test_190cm_is_valid_height(self):
        # given
        passport = """
        pid:087499704 hgt:190cm ecl:grn iyr:2012 eyr:2030 byr:1980
        hcl:#623a2f
        """

        # then
        assert is_passport_valid(passport)

    def test_149cm_is_invalid_height(self):
        # given
        passport = """
        pid:087499704 hgt:149cm ecl:grn iyr:2012 eyr:2030 byr:1980
        hcl:#623a2f
        """

        # then
        assert is_passport_valid(passport) is False

    def test_194cm_is_invalid_height(self):
        # given
        passport = """
        pid:087499704 hgt:194cm ecl:grn iyr:2012 eyr:2030 byr:1980
        hcl:#623a2f
        """

        # then
        assert is_passport_valid(passport) is False

    def test_is_invalid_height_when_no_unit(self):
        # given
        passport = """
        pid:087499704 hgt:190 ecl:grn iyr:2012 eyr:2030 byr:1980
        hcl:#623a2f
        """

        # then
        assert is_passport_valid(passport) is False


class TestHcl:
    @pytest.mark.parametrize("color,is_valid", [
        ("#123abc", True),
        ("#fffffd", True),
        ("#123abz", False),
        ("123abc", False),
    ])
    def test_check_hair_color(self, color, is_valid):
        # given
        passport = f"""
        pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
        hcl:{color}
        """

        # then
        assert is_passport_valid(passport) == is_valid


class TestEcl:
    @pytest.mark.parametrize("color,is_valid", [
        ('amb', True),
        ('blu', True),
        ('brn', True),
        ('gry', True),
        ('grn', True),
        ('hzl', True),
        ('oth', True),
        ("wat", False),
    ])
    def test_check_hair_color(self, color, is_valid):
        # given
        passport = f"""
        pid:087499704 hgt:74in ecl:{color} iyr:2012 eyr:2030 byr:1980
        hcl:#123abc
        """

        # then
        assert is_passport_valid(passport) == is_valid


class TestPid:
    @pytest.mark.parametrize("pid,is_valid", [
        ('000000001', True),
        ('087499704', True),
        ('0123456789', False),
    ])
    def test_check_pid(self, pid, is_valid):
        # given
        passport = f"""
        pid:{pid} hgt:74in ecl:hzl iyr:2012 eyr:2030 byr:1980
        hcl:#123abc
        """

        # then
        assert is_passport_valid(passport) == is_valid
