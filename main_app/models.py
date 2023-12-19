from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Set(models.Model):
    name = models.CharField(max_length=100)
    slug = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sets')

    class Meta:
        unique_together = ('user', 'name')


class Card(models.Model):
    front_side = models.CharField(max_length=250)
    back_side = models.CharField(max_length=250)
    set = models.ForeignKey(Set, on_delete=models.CASCADE, related_name='cards')
    create_reverse_card = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.front_side} - {self.back_side}'