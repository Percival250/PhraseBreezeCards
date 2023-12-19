from django.db import models

# Create your models here.
class Lending(models.Model):
    heading = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)

    def __str__(self):
        return self.heading

class Advantages(models.Model):
    advantages = models.CharField(max_length=100,null=True)
    advantage_description = models.CharField(max_length=100)
    def __str__(self):
        return self.advantages

class Feature(models.Model):
    feature = models.CharField(max_length=100)
    feature_description = models.CharField(max_length=100)
    def __str__(self):
        return self.feature
