# Generated by Django 3.2.13 on 2023-10-08 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShiftOrganizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
