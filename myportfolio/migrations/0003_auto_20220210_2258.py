# Generated by Django 3.1.3 on 2022-02-10 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0002_auto_20220210_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.FilePathField(default='', path='D:\\djngo projects\\portfolio\\simple\\New folder\\Portfolio-website-using-django-main\\myportfolio/static/img'),
        ),
    ]
