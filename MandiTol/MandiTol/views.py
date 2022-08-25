from django.shortcuts import render, redirect,HttpResponseRedirect
from django.http import HttpResponseRedirect

from decimal import *
from datetime import date

from Ledger.models import *


# Create your views here.
def start(response):
    if (response.method == "POST"):
        if (response.POST.get('start')):
            return redirect('tol/data')

        elif (response.POST.get('AdatTol')):
            return redirect('tol/AdatTolPage')

        elif (response.POST.get('TodaysTol')):
            return redirect('tol/TodaysTol')

        elif (response.POST.get('search')):
            return redirect('tol/search')

        elif (response.POST.get('averages')):
            return redirect('tol/averages')

        elif (response.POST.get('dailyAverage')):
            return redirect('tol/daily')
        elif (response.POST.get('createLedger')):
            return redirect('/ledger/createPage/')

        elif (response.POST.get('showBills')):
            return redirect('tol/bill')
        
        elif (response.POST.get('Khatabook')):
            return redirect('tol/Khatabook')
        else :
            return render(response, 'MandiTol/startTol.html', {})

    return render(response, 'MandiTol/startTol.html', {})