# Generated by Django 3.1.3 on 2022-02-12 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0006_auto_20220212_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
