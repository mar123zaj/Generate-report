from report_generator import file_exists, change_date_format, country_code, validate_number, validate_percent


class Test_file_exists:

    def test_False(self):
        assert file_exists('NotFile') == False

    def test_True(self):
        assert file_exists('README.md') == True

class Test_change_date_format:

    def test_NotproperData(self):
        assert change_date_format('??/2/15') == '-'

    def test_properData(self):
        assert change_date_format('01/22/2019') == '2019-01-22'
    def test_almostProperData(self):
        assert change_date_format('13/22/2019') == '-'


class Test_country_code:
    def test_properData1(self):
        assert country_code('Mandiana') == 'GIN'

    def test_properData2(self):
        assert country_code('Beroun') != 'XXX'

    def test_notProperData(self):
        assert country_code('NotRealSubdivision') == 'XXX'


class Test_validate_number:

    def test_properData(self):
        assert validate_number('31') == 31


    def test_notProperData(self):
        assert validate_number('A') == '?'
