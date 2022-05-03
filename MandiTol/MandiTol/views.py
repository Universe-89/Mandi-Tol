from django.shortcuts import render, redirect,HttpResponseRedirect
from django.http import HttpResponseRedirect

from decimal import *




# Create your views here.
def start(response):
    if (response.method == "POST"):
        if (response.POST.get('start')):
            return redirect('tol/data')

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
        else :
            return render(response, 'Tol/startTol.html', {})

    return render(response, 'Tol/startTol.html', {})