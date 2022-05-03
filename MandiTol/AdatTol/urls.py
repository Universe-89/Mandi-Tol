from django.urls import path
from . import views
from Ledger import views as v
urlpatterns = [
    path('',views.start, name="tol"),
    path('daily/',views.daily, name="daily"),
    path('data/',views.data, name="data"),
    path('test/',views.test, name="test"),
    path('ledger/',v.startPage, name="startpage"),
]