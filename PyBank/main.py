import os
import csv

csvpath = os.path.join("Resources\PyBank_budget_data.csv")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
 #create lists to store data    
    
     
    for column in csvreader:
        months = []
        profits = []

        months.append(column[0])
        #convert data from string to integer to sum
        profits.append(int(column[1]))

        Months = len(list(months))
        start = profits[0]
        Total = sum(profits)

    print(f"Total Months: {Months}")
    print(f"Total: {Total}")      

    
    


  

    


    
