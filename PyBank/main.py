import os
import csv

csvpath = os.path.join("Resources\PyBank_budget_data.csv")



with open(csvpath) as csvfile:
    budget_data = csv.reader(csvpath, delimiter=",")
    csv_header = next(budget_data)
    print(f"Header: {csv_header}")
    print(type(csv_header))
    


    


    
