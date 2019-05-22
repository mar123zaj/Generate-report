from requests.exceptions import RequestException, ConnectionError
import pycountry
import geocoder
import datetime
import csv
import chardet


def file_exists(file_path):
    try:
        f = open(file_path)
        f.close()
    except FileNotFoundError:
        return False
    return True


def change_date_format(date):
    try:
        date = datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d')
    except ValueError:
        return '-'
    return date


def country_code(subdivison):
    try:
        country_code = pycountry.subdivisions.lookup(subdivison).country_code
    except LookupError:
        return 'XXX'
    return pycountry.countries.get(alpha_2=country_code).alpha_3


def validate_number(number):
    try:
        number = int(number)
    except ValueError:
        return '?'
    return number


def validate_percent():
    pass

def prepare_report(file_name, headers=True, output_name='Report', report_date=datetime.date.today()):
    """ Prepare report from input data

    :param file_name: Name of input data file. Can be write without '.csv' on the end.
    :param headers: True or False if we want or don't want headers in output file. (default True)
    :param output_name: First part of output file name. (default 'Report')
    :param report_date: Second part of output file name. This is date of preparing report. (default this day)
    :type file_name: str
    :type headers: bool
    :type output_name: str
    :type report_date: str
    :return: Information if the report was generated without problems.
    """

    file_name += '.csv'

    # find encoding of input file
    encoding = encoding_type(file_name)

    with open(output_name + ' ' + str(raport_date) + '.csv', 'w', encoding='utf-8') as output_file, \
            open(file_name, encoding=encoding) as input_file:
        input_rows = list(csv.reader(input_file))
        report = csv.writer(output_file, delimiter=',', lineterminator='\n')  # lineterminator for Unix line endings

        # check if input file has headers
        if has_header(file_name, encoding):
            input_rows = input_rows[1:]

        # give headers to output file for data readability
        if headers:
            report.writerow(['Date', 'Country', 'Number of impressions', 'Number of clicks'])

        report_data = list()
        for date, subdivision, impressions, ctr in input_rows:
            report_rows = list()

            impressions = validate_number(impressions)



            try:
                impressions = int(line[2])
            except ValueError as e:
                return e

            ctr = validate_percent(ctr)

            # calculate number of clicks
            report_rows.append(round(impressions * ctr, 2))
            report_data.append(report_rows)

        # sort data by first column followed by second column
        sorted_data = sorted(report_data, key=lambda row: (row[0], row[1]))
        for line in sorted_data:
            report.writerow(line)
    return 'Everything went well.'


def has_header(filename, encoding):
    with open(filename, 'r', encoding=encoding) as csvfile:
        sample = csvfile.read(1024)
        has_header = csv.Sniffer().has_header(sample)
    return has_header


def encoding_type(filename):
    """Get encoding type of given file"""

    with open(filename, 'rb') as csvfile:
        rawdata = csvfile.read()
        result = chardet.detect(rawdata)
        encoding = result['encoding']
    return encoding


def find_country(city):
    """Find country from given city

    Description about Geonames:
    Geonames isn't an ideal solution because in some cases finds city even if it not suppose to find.
    E.g. for 'Unknown' he finds 'Annaba' city in Algeria; for '-' he finds 'Mvangane' city in Cameroon etc.
    Better way is to use Google API, but if we keep in mind that Geonames is free is not that bad option.
    In my opinion in this case geonames will be good enough.
    """
    if city in ['Unknown', '-', ''] or not (city.isalpha()):
        return 'XXX'
    else:
        try:
            g = geocoder.geonames(city, key='mar123zaj')
        except ConnectionError:
            return False
        except RequestException:
            return False
        except TimeoutError:
            return False
        else:
            try:
                country = pycountry.countries.lookup(g.country)
            except LookupError:
                return 'XXX'
            else:
                # three letter country code
                return country.alpha_3
