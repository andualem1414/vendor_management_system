import random, string
from django.shortcuts import render
from rest_framework import generics, serializers, mixins
from rest_framework.response import Response

from .models import HistoricalPerformance, Vendor
from .serializers import HistoricalPerformanceSerializer, VendorSerializer

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


class VendorDetailAPIView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_field = "pk"


class VendorUpdateAPIView(generics.UpdateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_field = "pk"


class VendorDeleteAPIView(generics.DestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_field = "pk"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"message": "Vendor deleted successfully"}, status=200)


class HistoricalPerformanceDetailsAPIView(
    generics.GenericAPIView,
):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer

    def get(self, request, pk):
        try:
            instance = self.queryset.get(vendor=pk)

        except HistoricalPerformance.DoesNotExist:
            return Response({"error": "Historical Performance not found"}, status=404)

        serializer = self.serializer_class(instance)

        return Response(serializer.data)
