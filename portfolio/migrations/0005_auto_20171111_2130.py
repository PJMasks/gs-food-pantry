# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-12 03:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_visit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='id',
        ),
        migrations.AddField(
            model_name='visit',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='portfolio.Client'),
        ),
        migrations.AddField(
            model_name='visit',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='visit',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='portfolio.Employee'),
        ),
        migrations.AddField(
            model_name='visit',
            name='status',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='visit',
            name='visit_number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
