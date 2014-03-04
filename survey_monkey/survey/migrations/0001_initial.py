# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Survey'
        db.create_table(u'survey_survey', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'survey', ['Survey'])

        # Adding model 'Question'
        db.create_table(u'survey_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.Survey'])),
        ))
        db.send_create_signal(u'survey', ['Question'])

        # Adding model 'CompletedSurvey'
        db.create_table(u'survey_completedsurvey', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.Survey'])),
        ))
        db.send_create_signal(u'survey', ['CompletedSurvey'])

        # Adding model 'Answer'
        db.create_table(u'survey_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.Question'])),
            ('completed_survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.CompletedSurvey'])),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'survey', ['Answer'])


    def backwards(self, orm):
        # Deleting model 'Survey'
        db.delete_table(u'survey_survey')

        # Deleting model 'Question'
        db.delete_table(u'survey_question')

        # Deleting model 'CompletedSurvey'
        db.delete_table(u'survey_completedsurvey')

        # Deleting model 'Answer'
        db.delete_table(u'survey_answer')


    models = {
        u'survey.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'completed_survey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['survey.CompletedSurvey']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['survey.Question']"})
        },
        u'survey.completedsurvey': {
            'Meta': {'object_name': 'CompletedSurvey'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['survey.Survey']"})
        },
        u'survey.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['survey.Survey']"})
        },
        u'survey.survey': {
            'Meta': {'object_name': 'Survey'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['survey']