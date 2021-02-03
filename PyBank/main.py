import os
import csv

csvpath = os.path.join("Resources\PyBank_budget_data.csv")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
 #create lists to store data    
    months = []
    profits = []   
    for column in csvreader:

        months.append(column[0])
        profits.append(column[1])

        TotalMonths = len(list(months))
        Total = int(sum(profits))

        

print(f"Total Months: {TotalMonths}",
       f"Total: {Total}")
    
    


  

    


    
