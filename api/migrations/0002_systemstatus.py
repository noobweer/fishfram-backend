# Generated by Django 5.1.6 on 2025-03-01 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('temperature', models.DecimalField(decimal_places=5, max_digits=8)),
                ('oxygen_level', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ph_level', models.DecimalField(decimal_places=2, max_digits=5)),
                ('orp_level', models.DecimalField(decimal_places=2, max_digits=5)),
                ('salinity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('water_level', models.DecimalField(decimal_places=2, max_digits=5)),
                ('turbidity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('amonia_content', models.DecimalField(decimal_places=2, max_digits=5)),
                ('nitrite_content', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'verbose_name_plural': 'System Status',
                'ordering': ['-timestamp'],
            },
        ),
    ]
