# Generated by Django 4.1.7 on 2023-04-27 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('B2bApp', '0004_companyinfo_franchise_company_banner_first_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='Company_brochure',
            field=models.FileField(blank=True, null=True, upload_to='Company_pdf'),
        ),
    ]