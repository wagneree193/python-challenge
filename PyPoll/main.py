import os
import csv

csvpath = os.path.join("Resources", "PyPoll_election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)

    VoterID = []
    County = []
    Candidate = []


    for column in csvreader:
        
        VoterID.append(column[0])
        County.append(column[1])
        Candidate.append(column[2])

    TotalVotes= len(list(VoterID))

print(f"Total Votes: {TotalVotes}")