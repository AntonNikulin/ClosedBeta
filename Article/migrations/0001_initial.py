# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'Article_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Body', self.gf('django.db.models.fields.TextField')()),
            ('Date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('Date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'Article', ['Article'])

        # Adding model 'Tag'
        db.create_table(u'Article_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'Article', ['Tag'])

        # Adding M2M table for field Articles on 'Tag'
        m2m_table_name = db.shorten_name(u'Article_tag_Articles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'Article.tag'], null=False)),
            ('article', models.ForeignKey(orm[u'Article.article'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tag_id', 'article_id'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'Article_article')

        # Deleting model 'Tag'
        db.delete_table(u'Article_tag')

        # Removing M2M table for field Articles on 'Tag'
        db.delete_table(db.shorten_name(u'Article_tag_Articles'))


    models = {
        u'Article.article': {
            'Body': ('django.db.models.fields.TextField', [], {}),
            'Date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'Date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Article'},
            'Title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Article.tag': {
            'Articles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Article.Article']", 'symmetrical': 'False'}),
            'Meta': {'object_name': 'Tag'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['Article']