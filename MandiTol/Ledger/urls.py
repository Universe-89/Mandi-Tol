from django.urls import path
from . import views

urlpatterns = [
    path('createPage/',views.createPage,name = "createPage"),

]