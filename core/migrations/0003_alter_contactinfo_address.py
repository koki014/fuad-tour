# Generated by Django 3.2.7 on 2021-09-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_slider_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Ünvan'),
        ),
    ]
