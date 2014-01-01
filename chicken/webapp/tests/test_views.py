from django.test import TestCase, Client
from webapp.models import SensorData


class ViewTests(TestCase):

    def setUp(self):
        pass

    def test_add_data(self):
        data_string = '2013-11-25 11:09:34,-91,D1,M1'
        c = Client()
        response = c.put('/add_data', data_string)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'OK')

        sd = SensorData.objects.first()
        self.assertEqual(sd.timestamp.strftime('%Y-%m-%d'), '2013-11-25')
        self.assertEqual(sd.signal, -91)
        self.assertEqual(sd.door_open, True)
        self.assertEqual(sd.motion_sensed, True)