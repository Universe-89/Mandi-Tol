from django.urls import path
from . import views

urlpatterns = [
    path('',views.start, name="tol"),
    path('data/',views.data, name="data"),
]