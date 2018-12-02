import os
# Module for reading CSV files
import csv

csvPath = os.path.join('budget.csv')

with open(csvPath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    rowCount = 0
    profitOfPreviousRow=0
    change = 0
    totalAvgChange = 0
    totalChange = 0
    minChange = 0
    maxChange = 0
    total = 0
    maxMonth=" "
    minMonth=" "
    
    # Read each row of data after the header
    for row in csvreader:
        rowCount += 1
        total += int(row[1])
        
        if rowCount == 1:
            profitOfPreviousRow=int(row[1]) 
        else:
            change = int(row[1])-profitOfPreviousRow
            if change < minChange:
                minChange = change
                minMonth=row[0]
            if change > maxChange:
                maxChange = change
                maxMonth=row[0]
            totalChange += change
            # Once change is calculated save current row value as previous row
            profitOfPreviousRow = int(row[1])

    totalAvgChange = totalChange / (rowCount-1)

    #print
    print (f"Total Months:{rowCount}")
    print(f"Total: {total}")
    print(f"Average  Change:{totalAvgChange}")
    print(f"Greatest Increase in Profits:{maxMonth} ($ {maxChange})")
    print(f"Greatest Decrease in Profits:{minMonth} ($ {minChange})")

    #printing the output to the file
    print(f"Total Months:{rowCount}", file=open("budgetAnalysisOutput.txt", "w"))
    print(f"Total: {total}", file=open("budgetAnalysisOutput.txt", "a"))
    print(f"Average  Change:{totalAvgChange}", file=open("budgetAnalysisOutput.txt", "a"))
    print(f"Greatest Increase in Profits:{maxMonth} ($ {maxChange})", file=open("budgetAnalysisOutput.txt", "a"))
    print(f"Greatest Decrease in Profits:{minMonth} ($ {minChange})", file=open("budgetAnalysisOutput.txt", "a"))





