# Generated by Django 4.1.2 on 2022-11-02 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(max_length=100000),
        ),
    ]