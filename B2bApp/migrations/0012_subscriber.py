# Generated by Django 4.1.3 on 2023-05-04 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("B2bApp", "0011_category_company_product_company_subcategory_company"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subscriber",
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
                ("email", models.EmailField(max_length=254)),
                ("name", models.CharField(max_length=254)),
                ("subscribed_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]