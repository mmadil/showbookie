# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Movie.seats'
        db.delete_column('movies_movie', 'seats')


    def backwards(self, orm):
        # Adding field 'Movie.seats'
        db.add_column('movies_movie', 'seats',
                      self.gf('django.db.models.fields.IntegerField')(default=120),
                      keep_default=False)


    models = {
        'movies.movie': {
            'Meta': {'ordering': "['-start_date', 'title']", 'object_name': 'Movie'},
            'anon_rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'anon_rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'timings': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['movies.Timing']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'user_rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'movies.timing': {
            'Meta': {'object_name': 'Timing'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['movies']