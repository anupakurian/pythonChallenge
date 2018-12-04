import os
# Module for reading CSV files
import csv
import sys
import datetime



us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

csvPath = os.path.join('employee.csv')
with open(csvPath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

 # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    employeeDetails = []
    
    ssnSplit=[]
    ssnMasked=""
    
    for row in csvreader:
        employeeRow=[]
        splitName = " "
        employeeRow.append(row[0])
        splitName = row[1].split(" ")
        employeeRow.append(splitName[0])
        employeeRow.append(splitName[1])
        employeeRow.append(datetime.datetime.strptime(row[2], '%d-%m-%Y').strftime('%m/%d/%Y'))
        ssnSplit=row[3].split("-")
        ssnMasked="***-"+"***-"+ssnSplit[2]
        employeeRow.append(ssnMasked)
        employeeRow.append(us_state_abbrev[row[4]])
        employeeDetails.append(employeeRow)

    print("EmpID,Name,DOB,SSN,State",file=open("employeeOutput.txt", "w" ))
    for employee in employeeDetails:
        print (employee)
        print(f"{employee}", file=open("employeeOutput.txt", "a"))



