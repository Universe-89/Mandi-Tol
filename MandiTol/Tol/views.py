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
            count                  = response.POST.get("totalGaadi")
            countInteger = int(count) - 1
            info.bags  = 0
            while(countInteger>=0):
                info.bags = info.bags + int(response.POST.get("bags" + str(countInteger)))
                countInteger = countInteger - 1

            # count = count - 1;

            info.weight            = int(info.bags) * int(response.POST.get("bharti"))
            info.save()

            return redirect('/')

        if (response.POST.get('next')):
            info                   = TolDiary()
            info.kisan_name        = response.POST.get("name")
            info.item_name         = response.POST.get("item_name")
            info.rate              = response.POST.get("rate")
            count                  = response.POST.get("totalGaadi")
            countInteger = int(count) - 1
            copy_count = countInteger
            info.bags  = 0
            while(countInteger>=0):
                info.bags = info.bags + int(response.POST.get("bags" + str(countInteger)))
                countInteger = countInteger - 1

            # count = count - 1;

            info.weight            = int(info.bags) * int(response.POST.get("bharti"))
            info.save()

            print("#####################")
            print(response.POST.get("driverName2"))
            last_gaddiwala_name = response.POST.get("driverName" + str(copy_count))
            print(last_gaddiwala_name)
            last_bags_loaded = response.POST.get("bags" + str(copy_count))
            last_capacity = int(response.POST.get("capacity" + str(copy_count))) - int(last_bags_loaded)
            print(last_bags_loaded)
  

            return render(response,"Tol/data.html",{"gaddi_wala":last_gaddiwala_name,"capacity":last_capacity})
    return render(response,"Tol/data.html",{"gaddi_wala":None,"capacity":None})

def test(response):
    return render(response,"Tol/test.html",{})