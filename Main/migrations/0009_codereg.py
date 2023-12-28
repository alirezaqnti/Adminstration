# Generated by Django 3.2.23 on 2023-12-27 08:25

import Main.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0008_alter_questonnair_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(default=Main.models.Generate, max_length=6, verbose_name='کد')),
                ('Phone', models.CharField(max_length=50, verbose_name='شماره همراه')),
                ('Email', models.CharField(max_length=50, verbose_name='ایمیل')),
                ('Active', models.BooleanField(default=True, verbose_name='وضعیت')),
                ('Created_At', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ ایجاد')),
            ],
            options={
                'verbose_name_plural': 'CodeRegs',
            },
        ),
    ]