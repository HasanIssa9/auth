# Generated by Django 4.1.1 on 2023-08-08 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_checkoutdetail_zipcode_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
