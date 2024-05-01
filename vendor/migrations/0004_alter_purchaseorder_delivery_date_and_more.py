# Generated by Django 5.0.4 on 2024-05-01 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_alter_purchaseorder_po_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='delivery_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Delivery Date'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='order_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Order Date'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(blank=True, choices=[('Placed', 'Placed'), ('Confirmed', 'Confirmed'), ('Declined', 'Declined'), ('Delivered', 'Delivered')], default='Placed', max_length=200, null=True, verbose_name='Status Of Order'),
        ),
    ]
