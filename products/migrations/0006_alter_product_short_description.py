# Generated by Django 4.0.6 on 2022-09-21 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_short_description_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True),
        ),
    ]