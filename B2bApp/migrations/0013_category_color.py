# Generated by Django 4.1.3 on 2023-05-05 04:26

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("B2bApp", "0012_subscriber"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="color",
            field=colorfield.fields.ColorField(
                default="#FF0000", image_field=None, max_length=18, samples=None
            ),
        ),
    ]
