# Generated by Django 5.1.6 on 2025-04-27 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_pooloptimalvalues_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poolstatistic',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]
