# Generated by Django 3.1 on 2023-01-10 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20230110_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='routesettings',
            name='num_vehicles',
            field=models.PositiveIntegerField(default=6),
        ),
    ]
