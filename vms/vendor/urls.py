from django.urls import path

from . import views


urlpatterns = [
    path("", views.VendorListCreateAPIView.as_view()),
    path("<int:pk>/", views.VendorDetailAPIView.as_view(), name="vendor-detail"),
    path("<int:pk>/update/", views.VendorUpdateAPIView.as_view(), name="vendor-update"),
    path("<int:pk>/delete/", views.VendorDeleteAPIView.as_view(), name="vendor-delete"),
    # Performance Metrics
    path(
        "<int:pk>/performance/",
        views.HistoricalPerformanceDetailsAPIView.as_view(),
    ),
]
