from unicodedata import name
from django.db import models
from django.core.validators import MinValueValidator 
from django.urls import reverse


# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.name
    def get_absolute_url(self): 
        """Construct the absolute URL for this Item."""
        return "/item/%i" % self.id
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(5000)])


class Order(models.Model):
    def __str__(self):
        return f'Order {self.id}'
    item = models.ManyToManyField(Item)
