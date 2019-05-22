from report_generator import file_exists, change_date_format

def test_file_exists_False():
    assert file_exists('NotFile') == False

def test_file_exists_True():
    assert file_exists('README.md') == True

def test_change_date_format_NotproperData():
    assert change_date_format('A') == 'XXX'