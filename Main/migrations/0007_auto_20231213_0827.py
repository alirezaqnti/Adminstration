# Generated by Django 3.2.23 on 2023-12-13 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_remove_address_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='questonnair',
            name='Active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AddField(
            model_name='respondent',
            name='Active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
    ]