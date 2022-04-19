# Generated by Django 4.0.1 on 2022-04-19 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmsp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='total_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_buying_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_discount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_marked_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_stock',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='profit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='total_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity_imported',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity_remaining',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity_sold',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
