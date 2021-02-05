import os
import csv

csvpath = os.path.join("Resources", "PyBank_budget_data.csv")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
 #create lists to store data    
    months = []
    profits = [] 
    monthly_change_list = []
    counter = 1
    greateast_profit = 0
    greateast_loss = 0
    prev_month_pl=0
    curr_month_pl=0
    month_profit=""
    month_loss=""
    Average = 0 
    for column in csvreader:
        
        
        months.append(column[0])
        #convert data from string to integer to sum
        profits.append(int(column[1]))
        #calculate the change over time in profits and add to list
        #next_profit=int(row[1])
        #change = (next_profit- profits[1])
        
        curr_month_pl=int(column[1])
        if counter > 1:
            month_change = curr_month_pl - prev_month_pl
            monthly_change_list.append(month_change)
            if greateast_profit < month_change:
                greateast_profit= month_change
                month_profit= column[0]
            if greateast_loss > month_change:
                greateast_loss = month_change
                month_loss=column[0]
        


        Months = len(list(months))
        start = profits[0]
        Total = sum(profits)
        #Average = sum(monthly_change_list)/(len(monthly_change_list))
        #Increase = max(profits)
        #Decrease = min(profits)
        prev_month_pl = int(column[1])
        counter=counter+1
    Average = round(sum(monthly_change_list)/(len(monthly_change_list)),2)  
    print(f"Total Months: {Months}")
    print(f"Total: {Total}")  
    print(f"Average Change: {Average}")
    print(f"Greatest Increase in Profits: {greateast_profit}, {month_profit}")
    print(f"Greatest Decrease in Profits: {greateast_loss}, {month_loss}")    

    
    


  

    


    
