# Generated by Django 4.1.3 on 2023-04-28 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("B2bApp", "0010_remove_companyinfo_company_url"),
        ("FranchiseApp", "0015_rename_mitsproducts_products"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Products",
            new_name="MitsProducts",
        ),
    ]
