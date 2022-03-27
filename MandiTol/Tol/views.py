from django.shortcuts import render, redirect,HttpResponseRedirect
from django.http import HttpResponseRedirect
from .models import TolDiary

# Create your views here.
def start(response):
    if (response.method == "POST"):
        if (response.POST.get('start')):
            return redirect('/data')
        else :
            return render(response, 'Tol/startTol.html', {})

    return render(response, 'Tol/startTol.html', {})

def data(response):
    if (response.method == "POST"):
        if (response.POST.get('submit')):
            info                   = TolDiary()
            info.kisan_name        = response.POST.get("name")
            info.item_name         = response.POST.get("item_name")
            info.rate              = response.POST.get("rate")
            # count                  = int(response.POST.get("driverCount")) - 1
            info.bags  = 0
            info.bags = info.bags + int(response.POST.get("bags1"))
            info.bags = info.bags + int(response.POST.get("bags2"))
            # count = count - 1;

            info.weight            = int(info.bags) * int(response.POST.get("bharti"))
            info.save()

            return redirect('/')
    return render(response,"Tol/data.html",{})

def test(response):
    return render(response,"Tol/test.html",{})