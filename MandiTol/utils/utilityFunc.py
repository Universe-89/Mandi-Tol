# All common functions are available here
from Ledger.models import *
from Tol.models import *
from datetime import date
def getDaywiseAdatPurchaseBillDetails(itemName) :
    billNums = BillMap.objects.filter(itemName=itemName,dateModified = date.today())

    bills = [] 
    for billNum in billNums:
            #bills.extend((Entry.objects.filter(billId = int(billNum.billId))))
        bills.append((Entry.objects.filter(billId = int(billNum.billId))))
    return bills

