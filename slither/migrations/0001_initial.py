# Generated by Django 2.1.1 on 2018-09-14 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('riddles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slither',
            fields=[
                ('riddle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='riddles.Riddle')),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
            ],
            bases=('riddles.riddle',),
        ),
        migrations.CreateModel(
            name='Square',
            fields=[
                ('slither_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='slither.Slither')),
            ],
            bases=('slither.slither',),
        ),
    ]
