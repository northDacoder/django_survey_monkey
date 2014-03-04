# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CompletedSurvey.title'
        db.add_column(u'survey_completedsurvey', 'title',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=300),
                      keep_default=False)

        # Adding field 'Question.survey'
        db.add_column(u'survey_question', 'survey',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['survey.Survey']),
                      keep_default=False)


        # Renaming column for 'Question.question' to match new field type.
        db.rename_column(u'survey_question', 'question_id', 'question')
        # Changing field 'Question.question'
        db.alter_column(u'survey_question', 'question', self.gf('django.db.models.fields.CharField')(max_length=300))
        # Removing index on 'Question', fields ['question']
        db.delete_index(u'survey_question', ['question_id'])


    def backwards(self, orm):
        # Adding index on 'Question', fields ['question']
        db.create_index(u'survey_question', ['question_id'])

        # Deleting field 'CompletedSurvey.title'
        db.delete_column(u'survey_completedsurvey', 'title')

        # Deleting field 'Question.survey'
        db.delete_column(u'survey_question', 'survey_id')


        # Renaming column for 'Question.question' to match new field type.
        db.rename_column(u'survey_question', 'question', 'question_id')
        # Changing field 'Question.question'
        db.alter_column(u'survey_question', 'question_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.Survey']))

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
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['survey.Survey']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'survey.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['survey.Survey']"})
        },
        u'survey.survey': {
            'Meta': {'object_name': 'Survey'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['survey']