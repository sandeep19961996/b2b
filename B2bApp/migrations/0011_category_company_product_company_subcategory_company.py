# Generated by Django 4.1.3 on 2023-05-04 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("B2bApp", "0010_remove_companyinfo_company_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="company",
            field=models.ManyToManyField(to="B2bApp.companyinfo"),
        ),
        migrations.AddField(
            model_name="product",
            name="company",
            field=models.ManyToManyField(to="B2bApp.companyinfo"),
        ),
        migrations.AddField(
            model_name="subcategory",
            name="company",
            field=models.ManyToManyField(to="B2bApp.companyinfo"),
        ),
    ]
