# Generated by Django 3.2.23 on 2023-11-28 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_auto_20231127_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='Name',
        ),
    ]