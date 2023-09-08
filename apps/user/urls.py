from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.user_list, name="user-list"),
]
