import os
import csv

csvpath = os.path.join("Resources\PyBank_budget_data.csv")

def budget_summary(budget_data):

    Months = str(budget_data[0])
    Profit = int(budget_data[1])

    TotalMonths = len(list(months))

    Total = sum(int(profits))

print(f"Total Months: {TotalMonths}",
       f"Total: {Total}")
    
    


  

    


    
