# Generated by Django 3.2.23 on 2023-11-30 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_remove_address_name'),
        ('Admins', '0007_auto_20231128_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personel',
            name='Address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.address', verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='personel',
            name='JobTitle',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='عنوان شغلی'),
        ),
        migrations.AlterField(
            model_name='personel',
            name='Joined',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ شروع همکاری'),
        ),
        migrations.AlterField(
            model_name='personel',
            name='Left',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ پایان همکاری'),
        ),
    ]
