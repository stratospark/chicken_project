# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'SensorData', fields ['timestamp', 'door_open']
        db.delete_unique(u'webapp_sensordata', ['timestamp', 'door_open'])

        # Adding unique constraint on 'SensorData', fields ['timestamp', 'signal', 'door_open', 'motion_sensed']
        db.create_unique(u'webapp_sensordata', ['timestamp', 'signal', 'door_open', 'motion_sensed'])


    def backwards(self, orm):
        # Removing unique constraint on 'SensorData', fields ['timestamp', 'signal', 'door_open', 'motion_sensed']
        db.delete_unique(u'webapp_sensordata', ['timestamp', 'signal', 'door_open', 'motion_sensed'])

        # Adding unique constraint on 'SensorData', fields ['timestamp', 'door_open']
        db.create_unique(u'webapp_sensordata', ['timestamp', 'door_open'])


    models = {
        u'webapp.sensordata': {
            'Meta': {'unique_together': "(('timestamp', 'signal', 'door_open', 'motion_sensed'),)", 'object_name': 'SensorData'},
            'door_open': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motion_sensed': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'signal': ('django.db.models.fields.SmallIntegerField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['webapp']