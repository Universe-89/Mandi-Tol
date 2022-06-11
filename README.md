MandiTol App
Landing page of all apps is in "MandiTol" App

Ledger App :
Here Ledgers are created 
model - "Ledger"

Tol app
Tol data is feteched in this app 
Adat Tol + direct Tol 
Adat Tol data is stored in "Entry" Table which is linked to "Ledger" table
Direct Tol data is stored in "TolDiary" Table 
StockRegister averages and Daily Tol data also in this app

DataBase Structure

TolDiary Table

Ledger Table 
        |Entry Table(Foriegn Key is Partyname because it is always unique)

StockRegister Table 
whole stock data is stored here

