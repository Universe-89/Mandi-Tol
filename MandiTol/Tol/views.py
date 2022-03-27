from django.shortcuts import render, redirect,HttpResponseRedirect
from django.http import HttpResponseRedirect

# Create your views here.
def start(response):
    if (response.method == "POST"):
        if (response.POST.get('start')):
            return redirect('/data')
        else :
            return render(response, 'Tol/startTol.html', {})

    return render(response, 'Tol/startTol.html', {})

def data(response):
    # if (response.method == "POST"):
    #     if (response.POST.get('save')):
    return render(response,"Tol/data.html",{})