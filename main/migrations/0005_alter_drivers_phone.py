# Generated by Django 4.0.1 on 2022-02-20 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_drivers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivers',
            name='phone',
            field=models.BigIntegerField(verbose_name='phone number'),
        ),
    ]
