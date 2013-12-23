# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'SensorData', fields ['timestamp']
        db.create_unique(u'webapp_sensordata', ['timestamp'])


    def backwards(self, orm):
        # Removing unique constraint on 'SensorData', fields ['timestamp']
        db.delete_unique(u'webapp_sensordata', ['timestamp'])


    models = {
        u'webapp.sensordata': {
            'Meta': {'object_name': 'SensorData'},
            'door_open': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motion_sensed': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'signal': ('django.db.models.fields.SmallIntegerField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['webapp']