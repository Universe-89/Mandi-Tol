from django.shortcuts import render, redirect,HttpResponseRedirect
from django.http import HttpResponseRedirect
from .models import *
from Ledger.models import *
from decimal import *




# Create your views here.
# def start(response):
#     if (response.method == "POST"):
#         if (response.POST.get('start')):
#             return redirect('/data')

#         elif (response.POST.get('TodaysTol')):
#             TolList = TolDiary.objects.all().order_by('-date_modified')
#             return render(response,'Tol/TolDiaryData.html', {"TolList":TolList})

#         elif (response.POST.get('search')):
#             name = response.POST.get("search_name")
#             stock_list = Stock_register.objects.get(item_name = name)
#             return render(response,'Tol/stock.html', {"stock_list":stock_list})

#         elif (response.POST.get('averages')):
#             stock_list = Stock_register.objects.all()
#             return render(response,'Tol/stock.html', {"stock_list":stock_list})

#         elif (response.POST.get('dailyAverage')):
#             return redirect('/daily')
#         elif (response.POST.get('createLedger')):
#             return redirect('/ledger/createPage/')
#         else :
#             return render(response, 'Tol/startTol.html', {})

#     return render(response, 'Tol/startTol.html', {})

def TodaysTol(response):
    TolList = TolDiary.objects.all().order_by('-date_modified')
    return render(response,'Tol/TolDiaryData.html', {"TolList":TolList})

def search(response):
    Tname = response.POST.get("search_name")
    stock_list = Stock_register.objects.get(item_name = name)
    return render(response,'Tol/stock.html', {"stock_list":stock_list})

def averages(response):
    stock_list = Stock_register.objects.all()
    return render(response,'Tol/stock.html', {"stock_list":stock_list})



def daily(response):
    itemList = Items.objects.all()
    if (response.method == "POST"):
        
        if (response.POST.get('submit')):
            date = response.POST.get("tol_day")
            item_name = response.POST.get("item_name")
            daily_register = TolDiary.objects.filter(item_name = item_name) 

            total_amount = 0
            total_weight = 0
            total_bags   = 0
            dhare_amount = 0
            expenses  = Items.objects.get(item_name = item_name)

            for tol in daily_register : 
                if(str(tol.date_modified) == str(date)):
                
                    dhare_amount = Decimal(tol.weight) * Decimal(tol.rate) / Decimal(100)
                    total_amount = total_amount + dhare_amount
                    total_weight = total_weight + Decimal(tol.weight)
                    total_bags   = total_bags   + Decimal(tol.bags)


            hamali = Decimal(total_bags) * Decimal(12)
            gaddi_bhada = Decimal(total_bags) * Decimal(5)
            tola = Decimal(total_bags) * Decimal(2)
            mandi_tax = Decimal(total_amount) * Decimal(expenses.mandi_tax) / Decimal(100)
            krishikalyan_ses = Decimal(total_amount) * Decimal(expenses.krishikalyan_ses) / Decimal(100)

            Grand_amount = total_amount + mandi_tax + krishikalyan_ses + hamali + gaddi_bhada + tola
            average = Grand_amount / total_weight * 100
            average = "{:.2f}".format(average)

            details = {"Grand_amount":Grand_amount,"total_weight":total_weight,"total_bags":total_bags,"hamali":hamali,"gaddi_bhada":gaddi_bhada,"tola":tola,
                        "mandi_tax":mandi_tax,"krishikalyan_ses":krishikalyan_ses,"average":average,"total_amount":total_amount,"date":date,
                        "item_name":item_name}

            return render(response,'Tol/dailyAvg.html', details)

            
    return render(response,'Tol/daily.html', { "itemList":itemList})


def data(response):
    itemList = Items.objects.all()
    ledgerList = Ledger.objects.all()
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
  

            return render(response,"Tol/data.html",{"gaddi_wala":last_gaddiwala_name,"capacity":last_capacity, "itemList":itemList ,"ledgerList":ledgerList})
    
    return render(response,"Tol/data.html",{"gaddi_wala":None,"capacity":None, "itemList":itemList ,"ledgerList":ledgerList})


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







    

