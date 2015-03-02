# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hobbie',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=128, verbose_name='Hobbie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('name', models.CharField(max_length=64, verbose_name='Language')),
                ('iso', models.CharField(serialize=False, primary_key=True, max_length=3, verbose_name='ISO')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('first_name', models.CharField(max_length=30, verbose_name='Firstname')),
                ('last_name', models.CharField(max_length=30, verbose_name='Lastname')),
                ('email', models.EmailField(max_length=75, verbose_name='Email')),
                ('birth_date', models.DateField(verbose_name='Birth date')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone number')),
                ('english_level', models.CharField(choices=[('never', 'Never'), ('beginner', 'Beginner'), ('fluent', 'Fluent')], max_length=10, verbose_name='English Level')),
                ('gender', models.CharField(choices=[('women', 'Women'), ('man', 'Man'), ('other', 'Other')], max_length=5, verbose_name='Gender')),
                ('participant_level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('indifferent', 'Indifferent')], max_length=12, verbose_name='participant level')),
                ('hobbie', models.ManyToManyField(related_name='person_mentor_related', to='person.Hobbie', null=True, blank=True, default=None)),
                ('language', models.ManyToManyField(related_name='person_mentor_related', to='person.Language', null=True, blank=True, default=None)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('name', models.CharField(max_length=64, verbose_name='Nationality')),
                ('iso', models.CharField(serialize=False, primary_key=True, max_length=3, verbose_name='ISO')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('first_name', models.CharField(max_length=30, verbose_name='Firstname')),
                ('last_name', models.CharField(max_length=30, verbose_name='Lastname')),
                ('email', models.EmailField(max_length=75, verbose_name='Email')),
                ('birth_date', models.DateField(verbose_name='Birth date')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone number')),
                ('english_level', models.CharField(choices=[('never', 'Never'), ('beginner', 'Beginner'), ('fluent', 'Fluent')], max_length=10, verbose_name='English Level')),
                ('gender', models.CharField(choices=[('women', 'Women'), ('man', 'Man'), ('other', 'Other')], max_length=5, verbose_name='Gender')),
                ('python_practice_since', models.CharField(choices=[('never', 'Never'), ('1year', '<1Year'), ('more', '>1year')], max_length=5, verbose_name='Python practice since')),
                ('django_practice_since', models.CharField(choices=[('never', 'Never'), ('1year', '<1Year'), ('more', '>1year')], max_length=5, verbose_name='Django practice since')),
                ('os', models.CharField(choices=[('mac', 'Mac'), ('linux', 'Linux'), ('win', 'windows')], max_length=20, verbose_name='Operating System')),
                ('Mentor', models.ForeignKey(related_name='participants', default=None, null=True, to='person.Mentor', blank=True)),
                ('hobbie', models.ManyToManyField(related_name='person_participant_related', to='person.Hobbie', null=True, blank=True, default=None)),
                ('language', models.ManyToManyField(related_name='person_participant_related', to='person.Language', null=True, blank=True, default=None)),
                ('nationality', models.ManyToManyField(related_name='person_participant_related', to='person.Nationality', null=True, blank=True, default=None)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mentor',
            name='nationality',
            field=models.ManyToManyField(related_name='person_mentor_related', to='person.Nationality', null=True, blank=True, default=None),
            preserve_default=True,
        ),
    ]
