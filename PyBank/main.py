import os
import csv

csvpath = os.path.join("Resources\PyBank_budget_data.csv")

Months = []
Profits = []
TotalMonths = []
Total = [] 
AverageChange = []
GreatestIncrease = []
GreatestDecrease = []

with open(csvpath) as csvfile:
    budget_data = csv.reader(csvpath, delimiter=",")
    for column in budget_data:
        Months.append(column[0])
        

        TotalMonths= len(list(Months))

print(f"Total Months: {TotalMonths}")
    
    


  

    


    
