from urllib import response
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.http import HttpResponseRedirect
from .models import *
# Create your views here.
def startPage(response):
    if(response.method == "POST"):
        if(response.POST.get('create')):
            return redirect('createPage')

    return render(response,'Ledger/startpage.html')

def createPage(response):
    
    if(response.method == "POST"):
        if(response.POST.get('submit')):
            info = Ledger()
            info.party_name = response.POST.get('name')
            info.partyAddress = response.POST.get('add')
            info.partyPincode = response.POST.get('pcode')
            info.partyCity  = response.POST.get('city')
            info.partyState = response.POST.get('state')
            info.partyOpBal = response.POST.get('opbal')

            info.save()

            return redirect('/')
    
    return render(response,'Ledger/create.html')


