from django.urls import path
from . import views

urlpatterns = [
    path("tambah/1", views.tambah1, name="tambah1"),
    path("tambah/2", views.tambah2, name="tambah2"),
]
