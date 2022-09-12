from django.contrib import admin
from stripeapi.models import Item, Order


admin.site.register(Item)
admin.site.register(Order)
# Register your models here.
