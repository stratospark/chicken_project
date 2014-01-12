from datetime import datetime
from mock import patch
import pytz
from webapp.utils import sunrise_and_sunset_for_date, _date_handler


@patch('webapp.utils.datetime')
def test_sunrise_and_sunset_for_date(mock_datetime):
    mock_datetime.today.return_value = datetime.strptime('2014-01-01 00:00:00', '%Y-%m-%d %H:%M:%S').replace(
        microsecond=0)
    sunrise, sunset = sunrise_and_sunset_for_date()
    assert sunrise.year == 2014 and sunrise.month == 1 and sunrise.hour == 7 and sunrise.minute == 21 and sunrise.second == 48
    assert sunset.year == 2014 and sunset.month == 1 and sunset.hour == 17 and sunset.minute == 1 and sunset.second == 22


def test_sunrise_and_sunset_for_date_given_date():
    sunrise, sunset = sunrise_and_sunset_for_date(
        datetime.strptime('2014-01-01 00:00:00', '%Y-%m-%d %H:%M:%S').
        replace(microsecond=0, tzinfo=pytz.timezone('US/Pacific')).
        astimezone(pytz.UTC))
    assert sunrise.year == 2014 and sunrise.month == 1 and sunrise.hour == 7 and sunrise.minute == 21 and sunrise.second == 48
    assert sunset.year == 2014 and sunset.month == 1 and sunset.hour == 17 and sunset.minute == 1 and sunset.second == 22


def test_date_handler_with_date():
    date = _date_handler(datetime(year=2000, month=1, day=1))
    assert date == '2000-01-01T00:00:00'


def test_date_handler_without_date():
    data = 'not a date'
    assert _date_handler(data) == data
