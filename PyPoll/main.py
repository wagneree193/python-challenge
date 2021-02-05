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
    Candidate_dict = {}
    Count=0
    Vote_Count=0
    Percent_Votes = 0
    Total_Votes = 0
    Winner = ""

    for row in csvreader:
        Count = Count + 1
        #Append data to lists
        VoterID.append(row[0])
        County.append(row[1])
        Candidate_list.append(row[2])
        #Create a set of unique words
        Candidate_set = set()
        Candidate_dict= dict()
        Candidate_dict = ("VoterID" : "Candidate_list")
        

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
print(f"Candidate: {Candidate_set}")