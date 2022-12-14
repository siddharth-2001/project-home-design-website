# Generated by Django 3.1 on 2020-08-21 14:15

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('phone', phone_field.models.PhoneField(help_text='Contact phone no.', max_length=31)),
                ('email', models.EmailField(max_length=254)),
                ('details', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('phone', phone_field.models.PhoneField(help_text='Contact phone no.', max_length=31)),
                ('email', models.EmailField(max_length=254)),
                ('rooms', models.TextField(max_length=156)),
                ('category', models.CharField(max_length=128)),
                ('area', models.FloatField()),
                ('address', models.TextField()),
                ('pincode', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
