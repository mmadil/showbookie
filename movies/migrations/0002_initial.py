# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Timing'
        db.create_table('movies_timing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('movies', ['Timing'])

        # Adding model 'Movie'
        db.create_table('movies_movie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=255, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('enable_comments', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('user_rating_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('user_rating_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('movies', ['Movie'])

        # Adding M2M table for field timings on 'Movie'
        db.create_table('movies_movie_timings', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm['movies.movie'], null=False)),
            ('timing', models.ForeignKey(orm['movies.timing'], null=False))
        ))
        db.create_unique('movies_movie_timings', ['movie_id', 'timing_id'])


    def backwards(self, orm):
        # Deleting model 'Timing'
        db.delete_table('movies_timing')

        # Deleting model 'Movie'
        db.delete_table('movies_movie')

        # Removing M2M table for field timings on 'Movie'
        db.delete_table('movies_movie_timings')


    models = {
        'movies.movie': {
            'Meta': {'ordering': "['-start_date', 'title']", 'object_name': 'Movie'},
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