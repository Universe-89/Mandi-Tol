
# from django.conf.urls import url
import imp
from django.urls import path, include
from .views import *

urlpatterns = [
    path('ledgerApi', LedgerListApiView.as_view()),
    path('itemApi', ItemApiView.as_view()),
]