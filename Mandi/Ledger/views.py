from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Ledger
from .serializers import LedgerSerializer

class LedgerListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    # def get(self, request, *args, **kwargs):
    #     '''
    #     List all the ledger items for given requested user
    #     '''
    #     serializer = LedgerSerializer(Ledger, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the ledger with given ledger data
        '''
        data = {
            'name'      : request.data.get('name'), 
            'address'   : request.data.get('address'), 
            'pincode'   : request.data.get('pincode'),
            'city'      : request.data.get('city'),
            'state'     : request.data.get('state'),
            'opBal'     : request.data.get('opBal'),
            'GSTIN'     : request.data.get('GSTIN'),
            'phoneNumber':request.data.get('phoneNumber'),
        }
        serializer = LedgerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)