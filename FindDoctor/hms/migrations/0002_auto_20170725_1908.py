# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-25 13:08
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='health_issue',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('chest pain', 'chest pain'), ('suffocation', 'suffocation'), ('stomachache', 'stomachache'), ('toothache', 'toothache'), ('fever', 'fever'), ('allergy', 'allergy'), ('std', 'std'), ('constipation', 'constipation'), ('diarrhea', 'diarrhea'), ('dysentery', 'dysentery'), ('ulcer', 'ulcer'), ('child disease', 'child disease'), ('gastric', 'gastric'), ('marital issues', 'marital issues'), ('headache', 'headache'), ('mental condition', 'mental condition'), ('broken bone', 'broken bone'), ('fracture', 'fracture'), ('stroke', 'stroke'), ('nervous problems', 'nervous problems'), ('seizure', 'seizure'), ('swallowing', 'swallowing')], max_length=50),
        ),
    ]
