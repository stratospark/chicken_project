from django.core.management import call_command
from django.db.utils import IntegrityError
from django.test import TestCase
from mock import patch, Mock


class ImportCSVTests(TestCase):
    @patch('__builtin__.open')
    @patch('webapp.management.commands.import_csv.reader')
    @patch('webapp.management.commands.import_csv.SensorData')
    def test_handle_default(self, mock_sensor_data, mock_reader, mock_open):
        test_data = ['2013-11-25 11:09:34,-91,D1,M1',
                     '2013-11-25 11:20:29,-89,D1,M1']
        mock_reader.return_value = iter(test_data)

        call_command('import_csv')
        mock_open.assert_called_with('../chickens.txt')

        mock_sensor_data.create_from_csv_row.has_calls(test_data)


    @patch('__builtin__.open')
    def test_handle_file_path(self, mock_open):
        file_path = 'chickens2.txt'
        call_command('import_csv', file_path)
        mock_open.assert_called_with(file_path)

    @patch('__builtin__.open')
    @patch('webapp.management.commands.import_csv.reader')
    @patch('webapp.management.commands.import_csv.SensorData')
    def test_handle_duplicate_entries(self, mock_sensor_data, mock_reader, mock_open):
        test_data = ['2013-11-25 11:09:34,-91,D1,M1',
                     '2013-11-25 11:09:34,-91,D1,M1']
        mock_reader.return_value = iter(test_data)

        # TODO: extract to separate class?
        mock_db_row = Mock()
        def _save():
            if mock_db_row.save.call_count == 2:
                raise IntegrityError
        mock_db_row.save.side_effect = _save

        mock_sensor_data.create_from_csv_row.return_value = mock_db_row
        mock_sensor_data.create_from_csv_row.has_calls(test_data)

        call_command('import_csv')
        mock_open.assert_called_with('../chickens.txt')
        assert mock_db_row.save.call_count == 2
