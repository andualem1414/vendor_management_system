from rest_framework import serializers
from .models import PurchaseOrder


class PurchaseOrderSerializer(serializers.ModelSerializer):
    po_number = serializers.CharField(read_only=True)

    class Meta:
        model = PurchaseOrder
        fields = "__all__"
        extra_fields = ["time_difference"]
