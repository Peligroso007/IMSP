# Generated by Django 4.0.1 on 2022-04-29 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inmsp', '0006_payment_now'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales',
            old_name='price',
            new_name='grand_total',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='product',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='profit',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='total_amount',
        ),
        migrations.AddField(
            model_name='payment',
            name='sales_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inmsp.sales'),
        ),
    ]