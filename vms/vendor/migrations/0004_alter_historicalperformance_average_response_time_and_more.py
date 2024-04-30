# Generated by Django 5.0.4 on 2024-04-30 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_remove_vendor_average_response_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalperformance',
            name='average_response_time',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='fullfillment_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='on_time_delivery_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='quality_rating_avg',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
