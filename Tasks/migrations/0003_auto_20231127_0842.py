# Generated by Django 3.2.23 on 2023-11-27 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0002_auto_20231127_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='SST',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='شماره ساب تسک'),
        ),
        migrations.AlterField(
            model_name='task',
            name='STA',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='شماره تسک'),
        ),
        migrations.AlterField(
            model_name='taskfile',
            name='STF',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='شماره فایل'),
        ),
    ]
