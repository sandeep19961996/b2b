# Generated by Django 4.1.7 on 2023-04-27 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FranchiseApp', '0010_mitsproducts_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edmundproducts',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='edmundproducts',
            name='pdf_file',
        ),
        migrations.RemoveField(
            model_name='medfenseproducts',
            name='banner_first',
        ),
        migrations.RemoveField(
            model_name='medfenseproducts',
            name='banner_second',
        ),
        migrations.RemoveField(
            model_name='medfenseproducts',
            name='banner_third',
        ),
        migrations.RemoveField(
            model_name='mitsproducts',
            name='banner_first',
        ),
        migrations.RemoveField(
            model_name='mitsproducts',
            name='banner_second',
        ),
        migrations.RemoveField(
            model_name='mitsproducts',
            name='banner_third',
        ),
        migrations.RemoveField(
            model_name='rapidproducts',
            name='banner_first',
        ),
        migrations.RemoveField(
            model_name='rapidproducts',
            name='banner_second',
        ),
        migrations.RemoveField(
            model_name='rapidproducts',
            name='banner_third',
        ),
        migrations.RemoveField(
            model_name='ronishproducts',
            name='banner_first',
        ),
        migrations.RemoveField(
            model_name='ronishproducts',
            name='banner_second',
        ),
        migrations.RemoveField(
            model_name='ronishproducts',
            name='banner_third',
        ),
        migrations.RemoveField(
            model_name='servoproducts',
            name='banner_first',
        ),
        migrations.RemoveField(
            model_name='servoproducts',
            name='banner_second',
        ),
        migrations.RemoveField(
            model_name='servoproducts',
            name='banner_third',
        ),
        migrations.RemoveField(
            model_name='shineproducts',
            name='banner_first',
        ),
        migrations.RemoveField(
            model_name='shineproducts',
            name='banner_second',
        ),
        migrations.RemoveField(
            model_name='shineproducts',
            name='banner_third',
        ),
    ]
