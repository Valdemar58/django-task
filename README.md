# django-task

Django + Stripe API backend.
You can find docker repository here: https://hub.docker.com/repository/docker/valdemar58/django-task

Database already contains 3 example Items, 1 Order and super user admin:admin.

Urls:
localhost:8000/item/<id:int> refers to the item page with the BUY button
localhost:8000/order/<id:int> refers to the order page with list of item names in order and the BUY button (order should be created manually in django.admin)
localhost:8000/buy/<id:int> creates stripe session and returns json response {"id": "sessionId"}
localhost:8000/make_order/<id:int> creates stripe session for order with multiple Items and returns json response {"id": "sessionId"}

Env variables:
DEBUG - debug mode in Django 1/0
DJANGO_ALLOWED_HOSTS
STRIPE_SECRET_KEY
STRIPE_PUBLIC_KEY
DJANGO_SECRET_KEY

