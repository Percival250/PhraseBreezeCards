from django.db import models
from django.contrib.auth.models import User

class SetCategory(models.Model):
    category = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category

    @classmethod
    def get_categories_for_choices(cls):
        return cls.objects.exclude(category='all categories')

    class Meta:
        verbose_name = 'Set category'
        verbose_name_plural = 'Set categories'

class Set(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100, blank=True)
    slug = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='library_sets')
    is_published = models.BooleanField(default=False, blank=True)
    cards_count = models.PositiveIntegerField()
    downloads = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(SetCategory, related_name='library_category', on_delete=models.CASCADE,
                                 default=1)

    def __str__(self):
        return f'{self.id} - {self.name} - {self.user}'


class Card(models.Model):
    front_side = models.CharField(max_length=250)
    back_side = models.CharField(max_length=250)
    set = models.ForeignKey(Set, on_delete=models.CASCADE, related_name='library_cards')

    def __str__(self):
        return f'{self.front_side} - {self.back_side}'
