from django.urls import path
from stripeapi import views


urlpatterns = [
    path('buy/<int:id>', views.buy, name='buy'),
    path('item/<int:id>', views.item, name='item'),
    path('order/<int:id>', views.order, name='order'),
    path('make_order/<int:id>', views.make_order, name='make_order'),
    
]
