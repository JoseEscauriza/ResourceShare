from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home-page"),
    path("resource/<int:id>", views.resource_detail, name="resource-detail"),
]
