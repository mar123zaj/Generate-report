from requests.exceptions import RequestException, ConnectionError
import pycountry
import geocoder
import datetime
import csv
import chardet

HEADERS = ['Date', 'Country', 'Number of impressions', 'Number of clicks']


def file_not_exists(file_path):
    try:
        f = open(file_path)
        f.close()
    except FileNotFoundError as e:
        print(e)
        return True
    return False


def change_date_format(date):
    try:
        date = datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d')
    except ValueError:
        return '-'
    return date


def country_code(subdivison):
    try:
        country_code = pycountry.subdivisions.lookup(subdivison).country_code
    except (LookupError, ConnectionError, RequestException, TimeoutError):
        return 'XXX'
    return pycountry.countries.get(alpha_2=country_code).alpha_3


def validate_number(number_string):
    try:
        number = int(number_string)
    except ValueError:
        return '?'
    return number


def validate_percent(percent_string):
    if '%' in percent_string:
        try:
            percent = float(percent_string.strip('%'))
        except ValueError:
            return '?'
        return percent/100
    else:
        return '?'


def prepare_report(file_name, output_name='Report'):
    """ Prepare report from input data"""

    file_name += '.csv'

    if file_not_exists(file_name):
        return None
    # find encoding of input file
    encoding = encoding_type(file_name)

    with open(f'{output_name} {datetime.date.today()}.csv', 'w', encoding='utf-8') as output_file, \
            open(file_name, encoding=encoding) as input_file:
        input_rows = list(csv.reader(input_file))
        report = csv.writer(output_file, delimiter=',', lineterminator='\n')  # lineterminator for Unix line endings

        # check if input file has headers
        if has_header(file_name, encoding):
            input_rows = input_rows[1:]


        report_data = list()
        for date, subdivision, impressions, ctr in input_rows:
            impressions = validate_number(impressions)
            ctr = validate_percent(ctr)
            if impressions == '?' or ctr == '?':
                clicks = '?'
            else:
                clicks = round(impressions * ctr)

        # sort data by first column followed by second column
        sorted_data = sorted(report_data, key=lambda row: (row[0], row[1]))
        for line in sorted_data:
            report.writerow(line)
    return 'Everything went well.'


def has_header(filename, encoding):
    with open(filename, 'r') as csvfile:
        sample = csvfile.read(1024)
    return csv.Sniffer().has_header(sample)


def encoding_type(filename):
    """Get encoding type of given file"""

    with open(filename, 'rb') as csvfile:
        rawdata = csvfile.read()
        result = chardet.detect(rawdata)
        encoding = result['encoding']
    return encoding

