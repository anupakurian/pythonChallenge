import os
# Module for reading CSV files
import csv


csvPath = os.path.join('electionData.csv')
rowcount = 0
electionSummary=[]

with open(csvPath, newline='') as csvfile:
   
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        rowFound=0

        for eachCandidate in electionSummary:
            if row[2] in eachCandidate:
                eachCandidate[1] += 1   
                rowFound = 1
        if rowFound == 0:
            candidateDetails = [row[2],1,0]
            electionSummary.append(candidateDetails)
        
        rowcount+=1
    

    #get the max vote
    maxVote=0
    winner=" "
    for candidate in electionSummary:
        if candidate[1] > maxVote:
            winner=candidate[0]
            maxVote=candidate[1]

    print ("Election Results")
    print ("-----------------------")
    print (f"Total Votes:{rowcount}")
    print ("-----------------------")
    
    for candidate in electionSummary:
        candidate[2]=round(candidate[1]/rowcount*100,3)
        print(f"{candidate[0]} : {candidate[2]} % ({candidate[1]})")

    print ("-----------------------")
    print(f"Winner: {winner}")
    print ("-----------------------")
        
    
#printing the output to the file
    print(f"Election Results", file=open("electionSummaryOutput.txt", "w"))
    print(f"-----------------------", file=open("electionSummaryOutput.txt", "a"))
    print(f"Total Votes:{rowcount}", file=open("electionSummaryOutput.txt", "a"))
    print(f"-----------------------", file=open("electionSummaryOutput.txt", "a"))

    for candidate in electionSummary:
        candidate[2]=round(candidate[1]/rowcount*100,3)
        print(f"{candidate[0]} : {candidate[2]} % ({candidate[1]})"\
        ,file=open("electionSummaryOutput.txt", "a"))

    print(f"-----------------------", file=open("electionSummaryOutput.txt", "a"))
    print(f"Winner: {winner}",\
        file=open("electionSummaryOutput.txt", "a"))
    print(f"-----------------------",\
        file=open("electionSummaryOutput.txt", "a"))
 







