# Generated by Django 5.1.6 on 2025-04-29 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_pool_ammonia_content_sensor_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pool',
            name='health_percents',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pool',
            name='health_zone',
            field=models.CharField(default=0, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pool',
            name='pool_name',
            field=models.CharField(default='Новый бассейн', max_length=100),
        ),
        migrations.AlterField(
            model_name='pool',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='pooloptimalvalues',
            name='max',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pooloptimalvalues',
            name='min',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='poolstatistic',
            name='ammonia_content',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='poolstatistic',
            name='nitrite_content',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='poolstatistic',
            name='orp',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='poolstatistic',
            name='oxygen_saturation',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='poolstatistic',
            name='pH',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='poolstatistic',
            name='salinity',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='poolstatistic',
            name='temperature',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='poolstatistic',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='poolstatistic',
            name='turbidity',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='poolstatistic',
            name='water_level',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='statisticarduino',
            name='ammonia_content',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='statisticarduino',
            name='nitrite_content',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='statisticarduino',
            name='orp',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='statisticarduino',
            name='oxygen_saturation',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='statisticarduino',
            name='pH',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='statisticarduino',
            name='salinity',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='statisticarduino',
            name='temperature',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='statisticarduino',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='statisticarduino',
            name='turbidity',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='statisticarduino',
            name='water_level',
            field=models.FloatField(default=0, null=True),
        ),
    ]
