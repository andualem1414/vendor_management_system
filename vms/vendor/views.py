import random, string
from django.shortcuts import render
from rest_framework import generics, serializers

from .models import Vendor
from .serializers import VendorSerializer

# Create your views here.


class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def random_code(self):
        vendor_code = "".join(
            random.choices(string.ascii_letters + string.digits, k=20)
        )

        # check if the code is already in the database.
        if Vendor.objects.filter(vendor_code=vendor_code).exists():
            return self.random_code()

        return vendor_code

    def perform_create(self, serializer):
        vendor_code = self.random_code()

        serializer.save(vendor_code=vendor_code)
