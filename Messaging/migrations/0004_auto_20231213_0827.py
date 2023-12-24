# Generated by Django 3.2.23 on 2023-12-13 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messaging', '0003_auto_20231127_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatfile',
            name='Active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='Active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AddField(
            model_name='chatparticipant',
            name='Active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AddField(
            model_name='chatthread',
            name='Active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AddField(
            model_name='messagelog',
            name='Active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AddField(
            model_name='threadlog',
            name='Active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
    ]