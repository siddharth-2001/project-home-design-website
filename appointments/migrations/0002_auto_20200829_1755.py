# Generated by Django 3.1 on 2020-08-29 12:25

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='amt_rooms',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote',
            name='budget',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote',
            name='property_type',
            field=models.CharField(default='Resedential', max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quote',
            name='rooms',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=6),
        ),
    ]
