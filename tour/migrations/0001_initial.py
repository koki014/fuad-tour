# Generated by Django 3.2.7 on 2021-09-21 13:56

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Antalya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Antalya/images')),
                ('prise', models.CharField(max_length=20)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('show_popular_tur', models.BooleanField(default=False, verbose_name='Tüm turlarda göstər')),
            ],
            options={
                'verbose_name': 'Antalya Tur',
                'verbose_name_plural': 'Antalya Turları',
            },
        ),
    ]
