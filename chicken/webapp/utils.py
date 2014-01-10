from datetime import datetime
import ephem
import pytz


def sunrise_and_sunset_for_date(date=None):
    home = ephem.Observer()
    home.lat = '37.354108'
    home.long = '-121.955236'

    if not date:
        today = datetime.today().replace(hour=0, minute=0, second=0)
        today = today.replace(tzinfo=pytz.timezone('US/Pacific'))
        today_utc = today.astimezone(pytz.UTC)
        date = today_utc

    sun = ephem.Sun()

    sunrise = ephem.localtime(home.next_rising(sun, start=date))
    sunset = ephem.localtime(home.next_setting(sun, start=date))
    return sunrise, sunset