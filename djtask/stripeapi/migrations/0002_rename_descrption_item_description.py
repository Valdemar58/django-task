# Generated by Django 4.1.1 on 2022-09-12 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stripeapi", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="item", old_name="descrption", new_name="description",
        ),
    ]
