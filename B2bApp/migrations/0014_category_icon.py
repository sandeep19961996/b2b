# Generated by Django 4.1.3 on 2023-05-05 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("B2bApp", "0013_category_color"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="icon",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]