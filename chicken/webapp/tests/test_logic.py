from datetime import datetime, timedelta
from django.test import TestCase
from mock import patch
from webapp.logic import ChickenLogic, ChickenStatus
from webapp.models import SensorData


@patch('webapp.logic.SensorData')
@patch('webapp.logic.sunrise_and_sunset_for_date')
@patch('webapp.logic.datetime')
class LogicTests(TestCase):
    TODAY = datetime(year=2014, month=1, day=15)
    TODAY_NOON = TODAY.replace(hour=12)
    TODAY_BEFORE_SUNRISE = TODAY.replace(hour=3)
    TODAY_SUNRISE = TODAY.replace(hour=6)
    TODAY_SUNSET = TODAY.replace(hour=18)
    TODAY_AFTER_SUNSET = TODAY.replace(hour=21)
    TOMORROW = TODAY + timedelta(days=1)
    TOMORROW_SUNRISE = TODAY_SUNRISE + timedelta(days=1)
    TOMORROW_SUNSET = TODAY_SUNSET + timedelta(days=1)

    @staticmethod
    def _setup_scenario(mock_datetime, mock_sunrise_sunset, mock_SensorData,
                        chickens_inside=True, door_open=True, now=None):
        mock_SensorData.get_latest.return_value = SensorData(timestamp=now, motion_sensed=chickens_inside,
                                                             door_open=door_open)
        mock_sunrise_sunset.side_effect = [
            (LogicTests.TODAY_SUNRISE, LogicTests.TODAY_SUNSET),
            (LogicTests.TOMORROW_SUNRISE, LogicTests.TOMORROW_SUNSET)
        ]

        mock_datetime.now.return_value = now

    ### Group 1
    def test_after_sunset_before_sunrise_chickens_inside_door_closed(self, mock_datetime, mock_sunrise_sunset,
                                                                     mock_SensorData):
        self._setup_scenario(mock_datetime, mock_sunrise_sunset, mock_SensorData,
                             chickens_inside=True, door_open=False, now=LogicTests.TODAY_AFTER_SUNSET)
        evaluation = ChickenLogic.evaluate_situation()
        assert evaluation.status == ChickenStatus.GOOD
        assert evaluation.message == ChickenStatus.ARE_PUT_AWAY


    def test_after_sunset_before_sunrise_chickens_outside_door_closed(self, mock_datetime, mock_sunrise_sunset,
                                                                      mock_SensorData):
        self._setup_scenario(mock_datetime, mock_sunrise_sunset, mock_SensorData,
                             chickens_inside=False, door_open=False, now=LogicTests.TODAY_AFTER_SUNSET)
        evaluation = ChickenLogic.evaluate_situation()
        assert evaluation.status == ChickenStatus.VERY_BAD
        assert evaluation.message == ChickenStatus.FIND_CHICKENS_CLOSE_DOOR


    def test_after_sunset_before_sunrise_chickens_inside_door_open(self, mock_datetime, mock_sunrise_sunset,
                                                                   mock_SensorData):
        self._setup_scenario(mock_datetime, mock_sunrise_sunset, mock_SensorData,
                             chickens_inside=True, door_open=True, now=LogicTests.TODAY_AFTER_SUNSET)
        evaluation = ChickenLogic.evaluate_situation()
        assert evaluation.status == ChickenStatus.VERY_BAD
        assert evaluation.message == ChickenStatus.CLOSE_DOOR


    def test_after_sunset_before_sunrise_chickens_outside_door_open(self, mock_datetime, mock_sunrise_sunset,
                                                                    mock_SensorData):
        self._setup_scenario(mock_datetime, mock_sunrise_sunset, mock_SensorData,
                             chickens_inside=False, door_open=True, now=LogicTests.TODAY_AFTER_SUNSET)
        evaluation = ChickenLogic.evaluate_situation()
        assert evaluation.status == ChickenStatus.VERY_BAD
        assert evaluation.message == ChickenStatus.FIND_CHICKENS_CLOSE_DOOR


    ### Group 2
    def test_after_sunrise_before_sunset_chickens_inside_door_closed(self, mock_datetime, mock_sunrise_sunset,
                                                                     mock_SensorData):
        self._setup_scenario(mock_datetime, mock_sunrise_sunset, mock_SensorData,
                             chickens_inside=True, door_open=False, now=LogicTests.TODAY_NOON)
        evaluation = ChickenLogic.evaluate_situation()
        assert evaluation.status == ChickenStatus.BAD
        assert evaluation.message == ChickenStatus.OPEN_DOOR


    def test_after_sunrise_before_sunset_chickens_outside_door_closed(self, mock_datetime, mock_sunrise_sunset,
                                                                      mock_SensorData):
        self._setup_scenario(mock_datetime, mock_sunrise_sunset, mock_SensorData,
                             chickens_inside=False, door_open=False, now=LogicTests.TODAY_NOON)
        evaluation = ChickenLogic.evaluate_situation()
        assert evaluation.status == ChickenStatus.BAD
        assert evaluation.message == ChickenStatus.OPEN_DOOR_FOR_NESTING


    def test_after_sunrise_before_sunset_chickens_inside_door_open(self, mock_datetime, mock_sunrise_sunset,
                                                                   mock_SensorData):
        self._setup_scenario(mock_datetime, mock_sunrise_sunset, mock_SensorData,
                             chickens_inside=True, door_open=True, now=LogicTests.TODAY_NOON)
        evaluation = ChickenLogic.evaluate_situation()
        assert evaluation.status == ChickenStatus.GOOD
        assert evaluation.message == ChickenStatus.MAYBE_NESTING


    def test_after_sunrise_before_sunset_chickens_outside_door_open(self, mock_datetime, mock_sunrise_sunset,
                                                                    mock_SensorData):
        self._setup_scenario(mock_datetime, mock_sunrise_sunset, mock_SensorData,
                             chickens_inside=False, door_open=True, now=LogicTests.TODAY_NOON)
        evaluation = ChickenLogic.evaluate_situation()
        assert evaluation.status == ChickenStatus.GOOD
        assert evaluation.message == ChickenStatus.ENJOYING_GARDEN
