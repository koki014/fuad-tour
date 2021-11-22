# Generated by Django 3.2.7 on 2021-09-23 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0017_day_tour'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tour/images')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.tour')),
            ],
            options={
                'verbose_name': 'Tur Şəkil ',
                'verbose_name_plural': 'Tur Şəkiləri',
            },
        ),
    ]
