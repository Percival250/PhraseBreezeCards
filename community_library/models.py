from django.db import models
from django.contrib.auth.models import User


class Set(models.Model):
    name = models.CharField(max_length=100)
    slug = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='library_sets')
    is_published = models.BooleanField(default=False, blank=True)
    cards_count = models.PositiveIntegerField()
    downloads = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.id} - {self.name} - {self.user}'


class Card(models.Model):
    front_side = models.CharField(max_length=250)
    back_side = models.CharField(max_length=250)
    set = models.ForeignKey(Set, on_delete=models.CASCADE, related_name='library_cards')

    def __str__(self):
        return f'{self.front_side} - {self.back_side}'
