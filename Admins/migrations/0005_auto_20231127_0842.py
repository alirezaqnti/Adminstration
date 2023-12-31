# Generated by Django 3.2.23 on 2023-11-27 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0004_rename_parent_team_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offdayrequest',
            name='SOD',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='شماره درخواست'),
        ),
        migrations.AlterField(
            model_name='personel',
            name='SRE',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='کد پرسنلی'),
        ),
        migrations.AlterField(
            model_name='team',
            name='ST',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='کد تیم'),
        ),
    ]
