# Generated by Django 3.2.23 on 2024-01-02 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0016_alter_personel_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personel',
            name='Picture',
            field=models.ImageField(max_length=500, upload_to='Admins/', verbose_name='تصویر پروفایل'),
        ),
    ]