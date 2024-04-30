from django.urls import path
from . import views

urlpatterns = [
    path("", views.PurchaseOrderListCreateAPIView.as_view()),
    path(
        "<int:pk>/",
        views.PurchaseOrderDetailAPIView.as_view(),
        name="purchase-order-detail",
    ),
    path(
        "<int:pk>/update/",
        views.PurchaseOrderUpdateAPIView.as_view(),
        name="purchase-order-update",
    ),
    path(
        "<int:pk>/delete/",
        views.PurchaseOrderDeleteAPIView.as_view(),
        name="purchase-order-delete",
    ),
    # Acknowledgment
    path("<int:pk>/acknowledge/", views.acknowledge, name="purchase-order/acknowledge"),
]
