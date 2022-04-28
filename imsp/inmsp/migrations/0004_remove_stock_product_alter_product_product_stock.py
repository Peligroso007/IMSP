# Generated by Django 4.0.1 on 2022-04-28 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inmsp', '0003_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='product',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_stock',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inmsp.stock'),
        ),
    ]
