from django.shortcuts import render, redirect,HttpResponseRedirect
from django.http import HttpResponseRedirect
from .models import TolDiary


# Create your views here.
def start(response):
    if (response.method == "POST"):
        if (response.POST.get('start')):
            return redirect('/data')
        elif (response.POST.get('TodaysTol')):
            TolList = TolDiary.objects.all()
            return render(response,'Tol/TolDiaryData.html', {"TolList":TolList})

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


            info.weight            = int(info.bags) * int(response.POST.get("bharti"))
            info.standardBharti    = response.POST.get("bharti")

            extraBharti = int(response.POST.get("extraBharti"))
            info.extra = extraBharti

            if(extraBharti != 0):
                info.weight = info.weight + extraBharti

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
            info.standardBharti    = response.POST.get("bharti")
            


            last_gaddiwala_name = response.POST.get("driverName"+ str(copy_count)) 
            last_bags_loaded = response.POST.get("bags" + str(copy_count))
            last_capacity = int(response.POST.get("capacity" + str(copy_count))) - int(last_bags_loaded)

            extraBharti = int(response.POST.get("extraBharti"))
            info.extra = extraBharti

            if(extraBharti != 0):
                info.weight = info.weight + extraBharti
                last_capacity = last_capacity - 1


            info.save()
  

            return render(response,"Tol/data.html",{"gaddi_wala":last_gaddiwala_name,"capacity":last_capacity})
    return render(response,"Tol/data.html",{"gaddi_wala":None,"capacity":None})

def test(response):
    return render(response,"Tol/test.html",{})