from rest_framework import serializers
from .models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    vendor_code = serializers.CharField(read_only=True)

    class Meta:
        model = Vendor
        fields = "__all__"
