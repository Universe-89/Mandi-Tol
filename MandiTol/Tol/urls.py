from django.urls import path
from . import views
from Ledger import views as v
urlpatterns = [
    # path('',views.start, name="tol"),
    path('daily/',views.daily, name="daily"),
    path('data/',views.data, name="data"),
    path('AdatTolPage/',views.AdatTolPage, name="AdatTolPage"),
    path('test/',views.test, name="test"),
    path('ledger/',v.startPage, name="startpage"),
    path('TodaysTol/',views.TodaysTol, name="TodaysTol"),
    path('search/',views.search, name="search"),
    path('averages/',views.averages, name="averages"),

    
]