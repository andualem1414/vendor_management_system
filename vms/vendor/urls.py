from django.urls import path

from . import views


urlpatterns = [
    path("", views.VendorListCreateAPIView.as_view()),
    # path("<int:pk>/", views.ExamDetailAPIView.as_view(), name="exam-detail"),
    # path("<int:pk>/delete/", views.ExamDestroyAPIView.as_view()),
    # path("<int:pk>/update/", views.ExamUpdateAPIView.as_view()),
]
