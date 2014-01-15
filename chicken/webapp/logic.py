from datetime import datetime, timedelta
from webapp.models import SensorData
from webapp.utils import sunrise_and_sunset_for_date


class ChickenStatus(object):
    GOOD = 1
    BAD = 0
    VERY_BAD = -1

    ARE_PUT_AWAY = 'Thanks for keeping us safe!'
    FIND_CHICKENS_CLOSE_DOOR = 'Find us and put us in the coop!'
    CLOSE_DOOR = 'Close the door! There might be opossums!'
    OPEN_DOOR = 'Hey, let us out!'
    OPEN_DOOR_FOR_NESTING = 'Hey, open the door in case we want to nest or eat!'
    MAYBE_NESTING = 'Seems like a good time to nest?'
    ENJOYING_GARDEN = 'We love playing in the garden!'

    def __init__(self, status, message):
        self.status = status
        self.message = message


class ChickenLogic(object):
    @classmethod
    def evaluate_situation(cls):
        current_time = datetime.now()
        latest_data = SensorData.get_latest()
        todays_sunrise, todays_sunset = sunrise_and_sunset_for_date()
        tomorrows_sunrise, tomorrows_sunset = sunrise_and_sunset_for_date(current_time + timedelta(days=1))

        status = None
        message = None
        if todays_sunset < current_time < tomorrows_sunrise:
            if latest_data.motion_sensed and not latest_data.door_open:
                status = ChickenStatus.GOOD
                message = ChickenStatus.ARE_PUT_AWAY
            elif not latest_data.motion_sensed and not latest_data.door_open:
                status = ChickenStatus.VERY_BAD
                message = ChickenStatus.FIND_CHICKENS_CLOSE_DOOR
            elif latest_data.motion_sensed and latest_data.door_open:
                status = ChickenStatus.VERY_BAD
                message = ChickenStatus.CLOSE_DOOR
            elif not latest_data.motion_sensed and latest_data.door_open:
                status = ChickenStatus.VERY_BAD
                message = ChickenStatus.FIND_CHICKENS_CLOSE_DOOR
        elif todays_sunrise < current_time < todays_sunset:
            if latest_data.motion_sensed and not latest_data.door_open:
                status = ChickenStatus.BAD
                message = ChickenStatus.OPEN_DOOR
            elif not latest_data.motion_sensed and not latest_data.door_open:
                status = ChickenStatus.BAD
                message = ChickenStatus.OPEN_DOOR_FOR_NESTING
            elif latest_data.motion_sensed and latest_data.door_open:
                status = ChickenStatus.GOOD
                message = ChickenStatus.MAYBE_NESTING
            elif not latest_data.motion_sensed and latest_data.door_open:
                status = ChickenStatus.GOOD
                message = ChickenStatus.ENJOYING_GARDEN

        return ChickenStatus(status, message)