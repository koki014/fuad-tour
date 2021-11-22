from django.db import models


class Logo(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='logo/images')

    def __str__(self):
        return f'{self.image.url}'

    class Meta:
        verbose_name = 'Loqo'
        verbose_name_plural = 'Loqo'


class Slider(models.Model):
    image = models.ImageField(upload_to='sliders/images/')

    def __str__(self):
        return f'{self.image.url}'

    class Meta:
        verbose_name = 'Slayder'
        verbose_name_plural = 'Slayderlər'


class ContactInfo(models.Model):
    phone = models.CharField(max_length=100, verbose_name="Əlaqə Nömrəsi")
    email = models.EmailField()
    address = models.CharField(max_length=100, verbose_name="Ünvan")

    def __str__(self):
        return f'Phone : {self.phone} ----  Email : {self.email}'

    class Meta:
        verbose_name = 'Əlaqə məlumatı'
        verbose_name_plural = 'Əlaqə məlumatları'


class SocialMedia(models.Model):
    media_types = (
        ('whatsapp', 'Whatsapp'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
    )
    media = models.CharField(unique=True, max_length=50, choices=media_types)
    url = models.URLField()

    def __str__(self):
        return f'Media : {self.media}'

    class Meta:
        verbose_name = 'Sosial Şəbəkə'
        verbose_name_plural = 'Sosial Şəbəkələr'


class Service(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    button_text = models.CharField(max_length=50)
    button_url = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Xidmət Tərkibi'
        verbose_name_plural = 'Xidmət Tərkibi'


class InfoBlock(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.title
