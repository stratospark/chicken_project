from datetime import datetime, timedelta
from webapp.models import SensorData
from webapp.utils import sunrise_and_sunset_for_date


class ChickenLogic(object):

    GOOD = 1
    BAD = 0
    VERY_BAD = -1

    @classmethod
    def evaluate_situation(cls):
        current_time = datetime.now()
        latest_data = SensorData.get_latest()
        todays_sunrise, todays_sunset = sunrise_and_sunset_for_date()
        tomorrows_sunrise, tomorrows_sunset = sunrise_and_sunset_for_date(current_time + timedelta(days=1))

        status = None
        if todays_sunset < current_time < tomorrows_sunrise:
            if latest_data.motion_sensed and not latest_data.door_open:
                status = ChickenLogic.GOOD
            elif not latest_data.motion_sensed and not latest_data.door_open:
                status = ChickenLogic.VERY_BAD
            elif latest_data.motion_sensed and latest_data.door_open:
                status = ChickenLogic.VERY_BAD
            elif not latest_data.motion_sensed and latest_data.door_open:
                status = ChickenLogic.VERY_BAD
        elif todays_sunrise < current_time < todays_sunset:
            if latest_data.motion_sensed and not latest_data.door_open:
                status = ChickenLogic.BAD
            elif not latest_data.motion_sensed and not latest_data.door_open:
                status = ChickenLogic.BAD
            elif latest_data.motion_sensed and latest_data.door_open:
                status = ChickenLogic.GOOD
            elif not latest_data.motion_sensed and latest_data.door_open:
                status = ChickenLogic.GOOD

        return status