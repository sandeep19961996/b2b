# Generated by Django 4.1.7 on 2023-04-27 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FranchiseApp', '0013_edmundproducts_medfenseproducts_rapidproducts_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EdmundProducts',
        ),
        migrations.DeleteModel(
            name='MedFenseProducts',
        ),
        migrations.DeleteModel(
            name='RapidProducts',
        ),
        migrations.DeleteModel(
            name='RonishProducts',
        ),
        migrations.DeleteModel(
            name='ServoProducts',
        ),
        migrations.DeleteModel(
            name='ShineProducts',
        ),
    ]