# Generated by Django 3.0.8 on 2020-08-14 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_2', '0002_auto_20200811_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
