import random, string
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.utils import timezone

from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer

# Create your views here.


class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        vendor = self.request.GET.get("vendor_id")

        if vendor:
            return qs.filter(vendor=vendor)

        return qs

    def random_code(self):
        po_number = "".join(random.choices(string.ascii_letters + string.digits, k=20))

        # check if the code is already in the database.
        if PurchaseOrder.objects.filter(po_number=po_number).exists():
            return self.random_code()

        return po_number

    def perform_create(self, serializer):
        po_number = self.random_code()

        serializer.save(po_number=po_number)


class PurchaseOrderDetailAPIView(generics.RetrieveAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = "pk"


class PurchaseOrderUpdateAPIView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = "pk"


class PurchaseOrderDeleteAPIView(generics.DestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = "pk"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"message": "PurchaseOrder deleted successfully"}, status=200)


@api_view(["POST"])
def acknowledge(request, pk=None, *args, **kwargs):
    purchase_order = PurchaseOrder.objects.get(pk=pk)

    purchase_order.acknowledgment_date = timezone.now()
    purchase_order.save()

    response = {
        "message": "Successfully acknowledged",
    }

    return Response(response)
