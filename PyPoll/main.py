import os
import csv

candidate = []
unique_candidate = [] 


csvpath = os.path.join('Resources','election_data.csv')
text_file = open("Output.txt", "w+")

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    #get a list of just the candidates
    for row in csvreader:
        candidate.append(row[2])
     
    # get list of unique candidates
    for i in candidate: 
        # check if exists in unique_list or not, if not add it 
        if i not in unique_candidate: 
            unique_candidate.append(i) 

    print ("Election Results")
    print ("-------------------------")
    print (f"Total Votes: {len(candidate)}")
    print ("-------------------------")

    text_file.write ("Election Results\n")
    text_file.write ("-------------------------\n")
    text_file.write (f"Total Votes: {len(candidate)}\n")
    text_file.write ("-------------------------\n")
    
    # now add a for loop to loop through and match unique candidates and count how many votes for each
    prev_count = 0
    for name in unique_candidate:
        candidate_count = 0
        candidate_percent = 0.0
        for row in candidate:
            if name == row:
                candidate_count += 1
        if candidate_count > prev_count:  #keeps track of the highest votes and updates 
            winner = name
            prev_count = candidate_count
        candidate_percent = (candidate_count / len(candidate) * 100)
        #print the total votes and percentage
        print (f"{name} : {round(candidate_percent,3)}% ({candidate_count}) ") #why is round not giving me 3 decimals
        text_file.write (f"{name} : {round(candidate_percent,3)}% ({candidate_count}) \n")

print ("-------------------------")   
print (f"Winner: {winner}")
print ("-------------------------")
text_file.write ("-------------------------\n")   
text_file.write (f"Winner: {winner}\n")
text_file.write ("-------------------------")