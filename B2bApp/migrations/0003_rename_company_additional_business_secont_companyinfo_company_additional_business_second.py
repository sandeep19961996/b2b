# Generated by Django 4.1.7 on 2023-04-26 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('B2bApp', '0002_rename_company_address_companyinfo_company_location_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyinfo',
            old_name='Company_additional_business_secont',
            new_name='Company_additional_business_second',
        ),
    ]
