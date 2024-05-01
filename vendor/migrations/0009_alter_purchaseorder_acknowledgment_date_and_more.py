# Generated by Django 5.0.4 on 2024-05-01 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0008_alter_purchaseorder_acknowledgment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='acknowledgment_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Acknoledgment Date'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='issue_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Issue Date'),
        ),
    ]
