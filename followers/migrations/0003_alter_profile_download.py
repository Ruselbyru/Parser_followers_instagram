# Generated by Django 3.2.6 on 2021-09-01 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followers', '0002_auto_20210901_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='download',
            field=models.BooleanField(default=True),
        ),
    ]
