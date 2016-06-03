# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-02 20:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0009_auto_20160602_2243'),
        ('sudoku', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sudoku',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='sudoku',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='sudoku',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sudoku',
            name='modified_on',
        ),
        migrations.RemoveField(
            model_name='sudoku',
            name='pattern',
        ),
        migrations.RemoveField(
            model_name='sudoku',
            name='riddle_type',
        ),
        migrations.RemoveField(
            model_name='sudoku',
            name='solution',
        ),
        migrations.AddField(
            model_name='sudoku',
            name='riddle_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='riddles.Riddle'),
            preserve_default=False,
        ),
    ]