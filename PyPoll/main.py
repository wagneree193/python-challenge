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
        #Candidate_set = set(Candidate_list)
        #for the values in candidate set, if the value is not in the candidate unique list already, append to it
        
            

            



                                                   
        
        Counter = Counter + 1
        #find unique candidate names in the dicionary
        #create vote count value in dictionary for each unique name
        #for value in Candidate_dict.values():
            #if not value in Vote_Count:
                #Vote_Count[value] = 1
            #else:
                #Vote_Count[value] = Vote_Count[value] + 1

       # for key, value in Vote_Count.items():
           # if Vote_Count[key]>Total_Votes:
                #Total_Votes = Vote_Count[key]
                #Winner = key
            
            #Vote_Count[key] = [value] + [round(100*(value/Total_Votes),2)]
    Vote_Count = len(list(VoterID))
       


    TotalVotes= Vote_Count

print(f"Total Votes: {TotalVotes}")
print(Candidate_dict)
#print(f"Candidate: {Candidate_unique}")