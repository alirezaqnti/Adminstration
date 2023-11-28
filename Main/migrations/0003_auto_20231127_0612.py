# Generated by Django 3.2.23 on 2023-11-27 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0002_initial'),
        ('Main', '0002_questonnair_respondent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questonnair',
            name='Creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admins.personel', verbose_name='ایجاد کننده'),
        ),
        migrations.AlterField(
            model_name='questonnair',
            name='DefaultForm',
            field=models.TextField(verbose_name='فرم پیشفرض'),
        ),
        migrations.AlterField(
            model_name='questonnair',
            name='Form',
            field=models.TextField(verbose_name='فرم'),
        ),
        migrations.AlterField(
            model_name='questonnair',
            name='SQ',
            field=models.CharField(max_length=10, verbose_name='شماره پرسشنامه'),
        ),
        migrations.AlterField(
            model_name='respondent',
            name='Form',
            field=models.TextField(verbose_name='فرم'),
        ),
        migrations.AlterField(
            model_name='respondent',
            name='Personel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admins.personel', verbose_name='کارمند'),
        ),
        migrations.AlterField(
            model_name='respondent',
            name='Questonnair',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.questonnair', verbose_name='پرسشنامه'),
        ),
        migrations.AlterField(
            model_name='respondent',
            name='SQR',
            field=models.CharField(max_length=10, verbose_name='شماره پاسخ'),
        ),
    ]
