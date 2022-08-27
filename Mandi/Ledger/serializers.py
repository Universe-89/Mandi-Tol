from rest_framework import serializers
from .models import Ledger
class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = ["name", "address", "pincode", "city", "state","opBal","GSTIN","phoneNumber"]
