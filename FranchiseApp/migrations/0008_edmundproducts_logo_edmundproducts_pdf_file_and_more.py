# Generated by Django 4.1.7 on 2023-04-25 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FranchiseApp', '0007_alter_send_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='edmundproducts',
            name='logo',
            field=models.ImageField(default=1, upload_to='edmundproductimage/logo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='edmundproducts',
            name='pdf_file',
            field=models.FileField(default=1, upload_to='edmundproductimage/pdfdata'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medfenseproducts',
            name='banner_first',
            field=models.ImageField(null=True, upload_to='medfensebanner'),
        ),
        migrations.AddField(
            model_name='medfenseproducts',
            name='banner_second',
            field=models.ImageField(null=True, upload_to='medfensebanner'),
        ),
        migrations.AddField(
            model_name='medfenseproducts',
            name='banner_third',
            field=models.ImageField(null=True, upload_to='medfensebanner'),
        ),
        migrations.AddField(
            model_name='mitsproducts',
            name='banner_first',
            field=models.ImageField(null=True, upload_to='mitshealthcarebanner'),
        ),
        migrations.AddField(
            model_name='mitsproducts',
            name='banner_second',
            field=models.ImageField(null=True, upload_to='mitshealthcarebanner'),
        ),
        migrations.AddField(
            model_name='mitsproducts',
            name='banner_third',
            field=models.ImageField(null=True, upload_to='mitshealthcarebanner'),
        ),
        migrations.AddField(
            model_name='rapidproducts',
            name='banner_first',
            field=models.ImageField(null=True, upload_to='rapidbanner'),
        ),
        migrations.AddField(
            model_name='rapidproducts',
            name='banner_second',
            field=models.ImageField(null=True, upload_to='rapidbanner'),
        ),
        migrations.AddField(
            model_name='rapidproducts',
            name='banner_third',
            field=models.ImageField(null=True, upload_to='rapidbanner'),
        ),
        migrations.AddField(
            model_name='ronishproducts',
            name='banner_first',
            field=models.ImageField(null=True, upload_to='ronishbanner'),
        ),
        migrations.AddField(
            model_name='ronishproducts',
            name='banner_second',
            field=models.ImageField(null=True, upload_to='ronishbanner'),
        ),
        migrations.AddField(
            model_name='ronishproducts',
            name='banner_third',
            field=models.ImageField(null=True, upload_to='ronishbanner'),
        ),
        migrations.AddField(
            model_name='servoproducts',
            name='banner_first',
            field=models.ImageField(null=True, upload_to='servobanner'),
        ),
        migrations.AddField(
            model_name='servoproducts',
            name='banner_second',
            field=models.ImageField(null=True, upload_to='servobanner'),
        ),
        migrations.AddField(
            model_name='servoproducts',
            name='banner_third',
            field=models.ImageField(null=True, upload_to='servobanner'),
        ),
        migrations.AddField(
            model_name='shineproducts',
            name='banner_first',
            field=models.ImageField(null=True, upload_to='shineprobanner'),
        ),
        migrations.AddField(
            model_name='shineproducts',
            name='banner_second',
            field=models.ImageField(null=True, upload_to='shineprobanner'),
        ),
        migrations.AddField(
            model_name='shineproducts',
            name='banner_third',
            field=models.ImageField(null=True, upload_to='shineprobanner'),
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(null=True, upload_to='edmundproductimage/edmundbanner')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='FranchiseApp.edmundproducts')),
            ],
        ),
    ]
