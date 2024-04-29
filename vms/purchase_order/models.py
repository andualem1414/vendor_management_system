from django.db import models

# Create your models here.


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100)
    vendor = models.ForeignKey("vendor.Vendor", on_delete=models.CASCADE)
    order_date = (models.DateTimeField(auto_now_add=True),)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)
    quality_rating = models.FloatField()
    issue
