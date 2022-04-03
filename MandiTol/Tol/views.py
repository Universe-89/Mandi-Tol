from django.shortcuts import render, redirect,HttpResponseRedirect
from django.http import HttpResponseRedirect
from .models import *
from decimal import *


# Create your views here.
def start(response):
    if (response.method == "POST"):
        if (response.POST.get('start')):
            return redirect('/data')

        elif (response.POST.get('TodaysTol')):
            TolList = TolDiary.objects.all().order_by('-date_modified')
            return render(response,'Tol/TolDiaryData.html', {"TolList":TolList})

        elif (response.POST.get('search')):
            name = response.POST.get("search_name")
            stock_list = Stock_register.objects.get(item_name = name)
            return render(response,'Tol/stock.html', {"stock_list":stock_list})

        elif (response.POST.get('averages')):
            stock_list = Stock_register.objects.all()
            return render(response,'Tol/stock.html', {"stock_list":stock_list})

        else :
            return render(response, 'Tol/startTol.html', {})

    return render(response, 'Tol/stock.html', {})

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
            info.standardBharti    = response.POST.get("bharti")

            extraBharti = int(response.POST.get("extraBharti"))
            info.extra = extraBharti

            if(extraBharti != 0):
                info.weight = info.weight + extraBharti
                info.bags = info.bags + 1

            updateStock(info.item_name,info.weight,info.rate,info.bags)

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
                info.bags = info.bags + 1

            updateStock(info.item_name,info.weight,info.rate,info.bags)


            info.save()
  

            return render(response,"Tol/data.html",{"gaddi_wala":last_gaddiwala_name,"capacity":last_capacity})
    return render(response,"Tol/data.html",{"gaddi_wala":None,"capacity":None})

def test(response):
    return render(response,"Tol/test.html",{})


def updateStock(item_name,weight,rate,bags):
    expenses  = Items.objects.get(item_name = item_name)
    dhare_amount = Decimal(weight) * Decimal(rate) / Decimal(100)
    mandi_tax = Decimal(dhare_amount) * Decimal(expenses.mandi_tax) / Decimal(100)
    krishikalyan_ses = Decimal(dhare_amount) * Decimal(expenses.krishikalyan_ses) / Decimal(100)
    hamali = Decimal(bags) * Decimal(12)
    gaddi_bhada = Decimal(bags) * Decimal(5)
    tola = Decimal(bags) * Decimal(2)
    dhare_amount = dhare_amount + mandi_tax + krishikalyan_ses + hamali + gaddi_bhada + tola

    register  = Stock_register.objects.get(item_name = item_name)    
    amount_new = Decimal(register.total_amount) + dhare_amount
    weight_new = Decimal(register.total_weight) + Decimal(weight)
    average_new = amount_new / weight_new

    # register.update(total_amount = amount_new,total_weight = weight_new,averge = average_new)
    register.total_amount = amount_new
    register.total_weight = weight_new
    register.average = average_new

    register.save()


def query(name = None):
    if name:
        recipes = bhav.objects.filter(name__contains = name)
    else:
        recipes = bhav.objects.all()
    return recipes
def search(response):
    
    if(name == None) :
        name = "FULLRESULT"

    if name=='FULLRESULT':
        result = query(None)
    else:
        result = query(name)

    context = {"stock_list" : result}
    return render(response,"frontpage/home.html",context)





    

