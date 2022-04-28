# Generated by Django 4.0.1 on 2022-04-19 12:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=50, null=True)),
                ('product_type', models.CharField(blank=True, max_length=20, null=True)),
                ('product_marked_price', models.IntegerField(blank=True, max_length=10, null=True)),
                ('product_discount', models.IntegerField(blank=True, max_length=10, null=True)),
                ('product_buying_price', models.IntegerField(blank=True, max_length=10, null=True)),
                ('product_stock', models.IntegerField(blank=True, max_length=20, null=True)),
                ('product_experies', models.DateTimeField(blank=True, null=True)),
                ('product_manufacture', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suppliers_name', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_remaining', models.IntegerField(blank=True, max_length=50, null=True)),
                ('quantity_imported', models.IntegerField(blank=True, max_length=50, null=True)),
                ('quantity_sold', models.IntegerField(blank=True, max_length=50, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inmsp.product')),
                ('suppliers', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inmsp.suppliers')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, max_length=10, null=True)),
                ('price', models.IntegerField(blank=True, max_length=20, null=True)),
                ('total_price', models.IntegerField(blank=True, max_length=20, null=True)),
                ('profit', models.IntegerField(blank=True, max_length=20, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inmsp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('role', models.IntegerField(default=1)),
                ('gender', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, max_length=10, null=True)),
                ('price', models.IntegerField(blank=True, max_length=20, null=True)),
                ('discount', models.IntegerField(blank=True, max_length=20, null=True)),
                ('total_amount', models.IntegerField(blank=True, max_length=20, null=True)),
                ('sales', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inmsp.sales')),
            ],
        ),
    ]