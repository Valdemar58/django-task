# Generated by Django 4.1.1 on 2022-09-12 02:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stripeapi", "0004_alter_item_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="price",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(5000)]
            ),
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item", models.ManyToManyField(to="stripeapi.item")),
            ],
        ),
    ]