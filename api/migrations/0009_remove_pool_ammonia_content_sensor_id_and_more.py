# Generated by Django 5.1.6 on 2025-04-29 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_pool_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pool',
            name='ammonia_content_sensor_id',
        ),
        migrations.RemoveField(
            model_name='pool',
            name='nitrite_content_sensor_id',
        ),
        migrations.RemoveField(
            model_name='pool',
            name='orp_sensor_id',
        ),
        migrations.RemoveField(
            model_name='pool',
            name='oxygen_saturation_sensor_id',
        ),
        migrations.RemoveField(
            model_name='pool',
            name='pH_sensor_id',
        ),
        migrations.RemoveField(
            model_name='pool',
            name='salinity_sensor_id',
        ),
        migrations.RemoveField(
            model_name='pool',
            name='temperature_sensor_id',
        ),
        migrations.RemoveField(
            model_name='pool',
            name='turbidity_sensor_id',
        ),
        migrations.RemoveField(
            model_name='pool',
            name='water_level_sensor_id',
        ),
    ]
