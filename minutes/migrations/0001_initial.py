# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MtgMinutes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('startTime', models.TimeField()),
                ('endTime', models.DateTimeField()),
                ('meetingType', models.CharField(default=b'GN', max_length=2, choices=[(b'SP', b'Special'), (b'GN', b'General'), (b'AG', b'Annual general Meeting')])),
            ],
        ),
        migrations.CreateModel(
            name='MtgMinutesItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveSmallIntegerField(verbose_name=b'Ordinal Ranking of Item on the MtgMinutes it belongs to')),
                ('title', models.CharField(max_length=100)),
                ('detail', models.TextField()),
                ('MtgMinutes', models.ForeignKey(to='minutes.MtgMinutes')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'The Full Name of the Organization, Committee, Team, or other Unit')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userName', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='user',
            field=models.ForeignKey(to='minutes.User'),
        ),
        migrations.AddField(
            model_name='mtgminutes',
            name='noteTaker',
            field=models.ForeignKey(to='minutes.User'),
        ),
        migrations.AddField(
            model_name='mtgminutes',
            name='user',
            field=models.ForeignKey(to='minutes.Organization'),
        ),
    ]
