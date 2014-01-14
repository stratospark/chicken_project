from django.test import TestCase
from model_mommy.mommy import make
from webapp.models import SensorData


class SensorDataTests(TestCase):
    DataString = '2013-11-25 11:09:34,-91,D1,M1'

    def setUp(self):
        pass

    def test_unicode(self):
        sd = SensorData.create_from_string(SensorDataTests.DataString)
        match_string = '%s, Door Open: %s, Motion Sensed: %s' % (sd.timestamp,
                                                                 sd.door_open,
                                                                 sd.motion_sensed)
        self.assertEqual(str(sd), match_string)

    def test_create_from_string(self):
        sd = SensorData.create_from_string(SensorDataTests.DataString)
        self.assertEqual(sd.timestamp.strftime('%Y-%m-%d'), '2013-11-25')
        self.assertEqual(sd.signal, -91)
        self.assertEqual(sd.door_open, True)
        self.assertEqual(sd.motion_sensed, True)

    def test_create_from_csv_row(self):
        row = SensorDataTests.DataString.split(',')
        sd = SensorData.create_from_csv_row(row)
        self.assertEqual(sd.timestamp.strftime('%Y-%m-%d'), '2013-11-25')
        self.assertEqual(sd.signal, -91)
        self.assertEqual(sd.door_open, True)
        self.assertEqual(sd.motion_sensed, True)

    def test_get_latest(self):
        _, _, latest = make(SensorData, 3)
        assert SensorData.get_latest() == latest