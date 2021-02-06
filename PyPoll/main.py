import os
import csv

csvpath = os.path.join("Resources", "PyPoll_election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
#designating variables for later calculations
    VoterID = []
    County = []
    Candidate_list = []
    Candidate_unique = []
    Candidate_dict = {'Khan' : 0 , 'Li' : 0, "O'Tooley" : 0, "Correy" : 0}
    Counter = 0
    Vote_Count=0
    Percent_Votes = 0
    Total_Votes = 0
    Winner = ""

    for row in csvreader:
        
        #Append data to lists
        VoterID.append(row[0])
        County.append(row[1])
        Candidate_list.append(row[2])
        name = row[2]
        #candidate name is key and value is how many votes they got


    
        Candidate_dict[name] = Candidate_dict[name]+1 
        for name, value in Candidate_dict.items():
            if Candidate_dict[name] > Vote_Count:

                Vote_Count = Candidate_dict[name]
                Winner = name
            
        
       
            

            



                                                   
        
        Counter = Counter + 1
        

       # for key, value in Vote_Count.items():
           # if Vote_Count[key]>Total_Votes:
                #Total_Votes = Vote_Count[key]
                #Winner = key
            
            #Vote_Count[key] = [value] + [round(100*(value/Total_Votes),2)]
    Total_Votes = len(list(VoterID))
    
    Khan_tot = int(Candidate_list.count("Khan"))
    Li_tot = int(Candidate_list.count("Li"))
    OT_tot = int(Candidate_list.count("O'Tooley"))
    Correy_tot = int(Candidate_list.count("Correy"))

    Khan_pct = round((Khan_tot/Total_Votes)*100,2)
    Li_pct = round((Li_tot/Total_Votes)*100,2)
    OTooley_pct = round((OT_tot/Total_Votes)*100,2)
    Correy_pct = round((Correy_tot/Total_Votes)*100,2)

    #Percent_Votes= [round(100*(Candidate_dict[name]/Total_Votes),2)]   


print("Election Results")
print("------------------------")
print(f"Total Votes: {Total_Votes}")
print("------------------------")

print(f"Khan : {Khan_pct, [Khan_tot]}")
print(f"Li : {Li_pct, [Li_tot]}")
print(f"O'Tooley : {OTooley_pct, [OT_tot]}")
print(f"Correy: {Correy_pct, [Correy_tot]}")
print("-------------------------")
print(f"Winner: {Winner}")

#print(f"Candidate: {Candidate_unique}")