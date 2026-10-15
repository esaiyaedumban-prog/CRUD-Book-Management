from django.db import models

# Create your models here.
class Book(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    price = models.IntegerField()

    def _str_(self):
        return self.Title