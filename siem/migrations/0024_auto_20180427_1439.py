# Generated by Django 2.0.4 on 2018-04-27 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siem', '0023_auto_20180424_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logevent',
            name='path',
            field=models.CharField(default='', max_length=384),
        ),
        migrations.AlterField(
            model_name='logevent',
            name='referrer',
            field=models.CharField(default='', max_length=400),
        ),
    ]