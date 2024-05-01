# Generated by Django 5.0.4 on 2024-05-01 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_alter_purchaseorder_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='acknowledgment_date',
            field=models.DateField(auto_now=True, null=True, verbose_name='Acknoledgment Date'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='delivery_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Delivery Date'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='issue_date',
            field=models.DateField(auto_now=True, null=True, verbose_name='Issue Date'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='order_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Order Date'),
        ),
    ]
