from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    image = models.ImageField(max_length=100, upload_to='developers/')
    age = models.PositiveIntegerField(verbose_name='Возраст')
    description = models.TextField(verbose_name='Укажите описание', blank=True)

    def __str__(self):
        return self.name