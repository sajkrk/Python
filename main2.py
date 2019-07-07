import os
import csv
num_votes = []
candidate = []

file = os.path.join("..", "Resources", "election_data.csv")

with open(file, newline='') as myCsvFile:
    csvReader =  csv.reader(myCsvFile, delimiter=',')
    next(csvReader)
    for row in csvReader:
        num_votes.append(row[0])
        candidate.append(row[2])
    
    # putting the unique candidate into set
    representative = list(set(candidate))
    
    #getting the individual candidate count
    individualVotes =[]
    for x in representative:
        individualVotes.append(candidate.count(x))
       
print("Total " + "Votes: " + str(len(num_votes)))
print("----------------------")

#printing the each representative's percent and total votes using loop       
for k in range(len(representative)):
        print((representative[k])+ ":" + str('{:.2%}'.format(individualVotes[k]/len(candidate))) + " "+ str(individualVotes[k]))
        print("------------------")
print(f"Winner: { representative[individualVotes.index(max(individualVotes))]}")
print("--------------------\n") 




 