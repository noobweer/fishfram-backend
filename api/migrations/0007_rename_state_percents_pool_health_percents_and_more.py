# Generated by Django 5.1.6 on 2025-04-29 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_pool_state_percents_pool_state_zone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pool',
            old_name='state_percents',
            new_name='health_percents',
        ),
        migrations.RenameField(
            model_name='pool',
            old_name='state_zone',
            new_name='health_zone',
        ),
    ]
