from report_generator import file_not_exists, change_date_format, country_code, validate_number, validate_percent


class TestFileNotExists:

    def test_false(self):
        assert file_not_exists('NotFile') == True

    def test_true(self):
        assert file_not_exists('README.md') == False

class TestChangeDateFormat:

    def test_not_proper_data(self):
        assert change_date_format('??/2/15') == '-'

    def test_properData(self):
        assert change_date_format('01/22/2019') == '2019-01-22'
    def test_almost_proper_data(self):
        assert change_date_format('13/22/2019') == '-'


class TestCountryCode:
    def test_proper_data1(self):
        assert country_code('Mandiana') == 'GIN'

    def test_proper_data2(self):
        assert country_code('Beroun') != 'XXX'

    def test_not_proper_data(self):
        assert country_code('NotRealSubdivision') == 'XXX'


class TestValidateNumber:

    def test_proper_data(self):
        assert validate_number('31') == 31


    def test_not_proper_data(self):
        assert validate_number('A') == '?'


class TestValidatePercent:

    def test_proper_string(self):
        assert validate_percent('37.5%') == 0.375

    def test_not_proper_string_number(self):
        assert validate_percent('3.2') == '?'

    def test_not_proper_string_chars(self):
        assert validate_percent('A7V%') == '?'
