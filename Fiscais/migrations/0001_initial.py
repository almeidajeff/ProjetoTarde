# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Prova'
        db.create_table(u'Fiscais_prova', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('concurso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['concursos.Concurso'])),
        ))
        db.send_create_signal(u'Fiscais', ['Prova'])

        # Adding model 'Sala'
        db.create_table(u'Fiscais_sala', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('local', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('predio', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('prova', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['concursos.Concurso'])),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'Fiscais', ['Sala'])


    def backwards(self, orm):
        # Deleting model 'Prova'
        db.delete_table(u'Fiscais_prova')

        # Deleting model 'Sala'
        db.delete_table(u'Fiscais_sala')


    models = {
        u'Fiscais.prova': {
            'Meta': {'object_name': 'Prova'},
            'concurso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['concursos.Concurso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Fiscais.sala': {
            'Meta': {'object_name': 'Sala'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'predio': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'prova': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['concursos.Concurso']"})
        },
        u'concursos.concurso': {
            'Meta': {'object_name': 'Concurso'},
            'data': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['Fiscais']