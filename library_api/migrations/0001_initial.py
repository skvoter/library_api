# Generated by Django 2.2.8 on 2019-12-03 20:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('date_of_publishing', models.DateField(default=datetime.date(1970, 1, 1))),
                ('available', models.BooleanField(default=True)),
                ('reader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='books', to='library_api.Reader')),
            ],
        ),
    ]