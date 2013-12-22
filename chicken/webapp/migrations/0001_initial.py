# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SensorData'
        db.create_table(u'webapp_sensordata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('signal', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('door_open', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('motion_sensed', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'webapp', ['SensorData'])


    def backwards(self, orm):
        # Deleting model 'SensorData'
        db.delete_table(u'webapp_sensordata')


    models = {
        u'webapp.sensordata': {
            'Meta': {'object_name': 'SensorData'},
            'door_open': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motion_sensed': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'signal': ('django.db.models.fields.SmallIntegerField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['webapp']