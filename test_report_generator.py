from report_generator import file_exists, change_date_format, country_code


def test_file_exists_False():
    assert file_exists('NotFile') == False


def test_file_exists_True():
    assert file_exists('README.md') == True


def test_change_date_format_NotproperData():
    assert change_date_format('??/2/15') == '-'


def test_change_date_format_properData():
    assert change_date_format('01/22/2019') == '2019-01-22'


def test_change_date_format_almostProperData():
    assert change_date_format('13/22/2019') == '-'


def test_country_code_properData1():
    assert country_code('Mandiana') == 'GIN'


def test_country_code_properData2():
    assert country_code('Beroun') != 'XXX'


def test_country_code_notProperData():
    assert country_code('NotRealSubdivision') == 'XXX'
