# Generated by Django 4.1.7 on 2023-04-25 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FranchiseApp', '0006_ronishproducts_servoproducts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='send',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]