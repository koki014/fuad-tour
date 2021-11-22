from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=55)
    number = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ölkə'
        verbose_name_plural = 'Ölkələr'
        ordering = ('number',)


class Day(models.Model):
    name = models.CharField(max_length=55)
    number = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gün'
        verbose_name_plural = 'Günlər'
        ordering = ('number',)


class Tour(models.Model):
    days = models.ManyToManyField(Day, verbose_name='Günlər')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Ölkə')
    show_popular = models.BooleanField(default=False, verbose_name='Tüm turlarda göstər')
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tour/images')
    price = models.CharField(max_length=20)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tur'
        verbose_name_plural = 'Turlar'


class TourImage(models.Model):
    image = models.ImageField(upload_to='Tour/images')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'Tur Şəkil '
        verbose_name_plural = 'Tur Şəkiləri'


class Reservation(models.Model):
    user = models.CharField(max_length=100, verbose_name="Ad,Soyad")
    email = models.EmailField()
    phone = models.CharField(max_length=100, verbose_name="Telefon Nömrəsi")
    date = models.DateField(verbose_name="Tur Tarixi")
    adult = models.CharField(max_length=100, verbose_name="Böyük")
    child = models.CharField(max_length=100, verbose_name="Uşaq 2-12")
    baby = models.CharField(max_length=100, verbose_name="Uşaq 0-2")
    name_tour = models.ForeignKey(Tour, on_delete=models.CASCADE, blank=True, null=False)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Sifariş'
        verbose_name_plural = 'Sifarişler'
