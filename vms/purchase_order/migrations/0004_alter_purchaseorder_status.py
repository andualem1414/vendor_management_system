# Generated by Django 5.0.4 on 2024-04-30 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0003_purchaseorder_on_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(choices=[('COMPLETED', 'Completed'), ('PENDING', 'Pending'), ('CANCELED', 'Canceled')], max_length=100),
        ),
    ]
