# Generated by Django 3.1.1 on 2023-01-04 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20230104_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='code',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
