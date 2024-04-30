from django.db import models
from django.db.models.signals import post_save, post_delete, pre_save
from django.utils import timezone

from vendor.models import HistoricalPerformance
from django.db.models import Sum, Avg
from datetime import timedelta

# Create your models here.


class PurchaseOrder(models.Model):
    STATUS_CHOICES = (
        ("COMPLETED", "Completed"),
        ("PENDING", "Pending"),
        ("CANCELED", "Canceled"),
    )

    po_number = models.CharField(max_length=20)
    vendor = models.ForeignKey("vendor.Vendor", on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    on_time = models.BooleanField(null=True, blank=True)


def get_on_time_delivery_rate(vendor):

    completed_pos = PurchaseOrder.objects.filter(
        status="COMPLETED", vendor=vendor
    ).count()

    on_time_pos = PurchaseOrder.objects.filter(
        status="COMPLETED", vendor=vendor, on_time=True
    ).count()

    return on_time_pos / completed_pos if completed_pos > 0 else None


def get_quality_rating_avg(vendor):

    queryset = PurchaseOrder.objects.filter(status="COMPLETED", vendor=vendor)
    quality_rating_avg = queryset.aggregate(avg=Avg("quality_rating"))["avg"]

    return quality_rating_avg


def get_average_response_time(vendor):
    queryset = PurchaseOrder.objects.filter(vendor=vendor)

    total_pos = 0
    total_time_diff = 0
    for item in queryset:
        if item.acknowledgment_date:
            total_pos += 1
            total_time_diff += (item.acknowledgment_date - item.issue_date).microseconds

    return total_time_diff / total_pos if total_pos > 0 else None


def get_fullfillment_rate(vendor):
    queryset = PurchaseOrder.objects.filter(vendor=vendor)

    total = queryset.count()
    completed_total = queryset.filter(status="COMPLETED").count()

    return completed_total / total if total > 0 else None


def update_performance_metrics(sender, instance, **kwargs):
    purchase_order = instance
    vendor = instance.vendor

    on_time_delivery_rate = get_on_time_delivery_rate(vendor)
    quality_rating_avg = get_quality_rating_avg(vendor)
    average_response_time = get_average_response_time(vendor)
    fullfillment_rate = get_fullfillment_rate(vendor)

    historical_performance, created = HistoricalPerformance.objects.get_or_create(
        vendor=vendor
    )

    historical_performance.on_time_delivery_rate = on_time_delivery_rate
    historical_performance.quality_rating_avg = quality_rating_avg
    historical_performance.fullfillment_rate = fullfillment_rate
    historical_performance.average_response_time = average_response_time

    historical_performance.save()
    print("Signal received: ", purchase_order)


def update_on_time(sender, instance, **kwargs):
    purchase_order = instance

    try:
        prev_purchase_order = PurchaseOrder.objects.get(pk=purchase_order.id)
    except PurchaseOrder.DoesNotExist:
        print("Previous Purchase Order not found")
        return

    if (
        prev_purchase_order.status != "COMPLETED"
        and purchase_order.status == "COMPLETED"
    ):
        if purchase_order.delivery_date > timezone.now():
            onTime = True
        else:
            onTime = False

        purchase_order.on_time = onTime


post_save.connect(update_performance_metrics, sender=PurchaseOrder)
pre_save.connect(update_on_time, sender=PurchaseOrder)
