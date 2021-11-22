# Generated by Django 3.2.7 on 2021-09-22 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_contactinfo_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rezerv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100, verbose_name='Ad,Soyad,')),
                ('phone', models.CharField(max_length=100, verbose_name='Telefon Nömrəsi')),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField(verbose_name='Tur Tarixi')),
                ('adult', models.CharField(max_length=100, verbose_name='Böyük')),
                ('child', models.CharField(max_length=100, verbose_name='Uşaq 2-12')),
                ('baby', models.CharField(max_length=100, verbose_name='Uşaq 0-2')),
            ],
            options={
                'verbose_name': 'Sifariş',
                'verbose_name_plural': 'Sifarişler',
            },
        ),
    ]
