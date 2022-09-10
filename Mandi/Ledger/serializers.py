from rest_framework import serializers
from .models import *
class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = ["name", "address", "pincode", "city", "state","opBal","GSTIN","phoneNumber"]


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["name", "hsnCode", "mandiTax", "krishiKalyanCess", "aadat"]
