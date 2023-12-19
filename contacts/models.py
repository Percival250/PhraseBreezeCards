from django.db import models

# Create your models here.
class Contacts(models.Model):
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=14, default='+996')
    telegram_media_link = models.URLField(max_length=200)
    instagram_media_link = models.URLField(max_length=200)
    def __str__(self):
        return self.email