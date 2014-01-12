from datetime import datetime
import json
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

    sunrise = ephem.localtime(home.next_rising(sun, start=date)).replace(microsecond=0)
    sunset = ephem.localtime(home.next_setting(sun, start=date)).replace(microsecond=0)
    return sunrise, sunset


def _date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


def our_json_dumps(data):
    return json.dumps(data, default=_date_handler)


def _load_with_datetime(pairs, format='%Y-%m-%d'):
    """Load with dates"""
    d = {}
    for k, v in pairs:
        if isinstance(v, basestring):
            try:
                d[k] = datetime.strptime(v, format).date()
            except ValueError:
                d[k] = v
        else:
            d[k] = v
    return d


def our_json_loads(data):
    return json.loads(data, object_pairs_hook=_load_with_datetime)
