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
    #create variables for the calculations
    #make counter to skip the first row of data in the profits/losses
    counter = 1
    greatest_profit = 0
    greatest_loss = 0
    prev_month_pl=0
    curr_month_pl=0
    month_profit=""
    month_loss=""
    Average = 0 
    for row in csvreader:
        
        #designate data for months and profits lists
        months.append(row[0])
        #convert data from string to integer to sum
        profits.append(int(row[1]))

        #counter>1 will skip calculation on first row
        curr_month_pl=int(row[1])
        if counter > 1:
            month_change = curr_month_pl - prev_month_pl
            #add calculations to a list
            monthly_change_list.append(month_change)
            #change the month_change variable every time a higher value is encountered for greatest profit;lower for greatest loss
            #match the corresponding month
            if greatest_profit < month_change:
                greatest_profit= month_change
                month_profit= row[0]
            if greatest_loss > month_change:
                greatest_loss = month_change
                month_loss=row[0]
        


        Months = len(list(months))
        #start = profits[0]
        Total = sum(profits)
        prev_month_pl = int(row[1])
        counter=counter+1

    #put average outside of the loop bc monthly change list is not final until the loop completes
    #round to two decimal places    
    Average = round(sum(monthly_change_list)/(len(monthly_change_list)),2)  

    #print outputs from calculations
    print(f"Total Months: {Months}")
    print(f"Total: {Total}")  
    print(f"Average Change: {Average}")
    print(f"Greatest Increase in Profits: {month_profit}, {greatest_profit}")
    print(f"Greatest Decrease in Profits: {month_loss}, {greatest_loss}")    

    
    


  

    


    
