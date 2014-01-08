from django.test import TestCase, Client
from model_mommy import mommy
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

    def test_add_data_fail(self):
        data_string = '2013-1,-91,D1,M1'
        c = Client()
        response = c.put('/add_data', data_string)
        self.assertEqual(response.status_code, 400)
        self.assertNotEqual(response.content, 'OK')

        self.assertEqual(SensorData.objects.count(), 0)

    def test_index(self):
        sensor_data = mommy.make('SensorData', door_open=False)
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code , 200)
        self.assertEqual(response.context['chickens_put_away'], True)
        self.assertEqual(response.context['last_updated'], sensor_data.timestamp)