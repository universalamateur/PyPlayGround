#!/usr/bin/env python3

import re
import csv
import operator
import sys

"""one CSV is a ranking of errors generated by the system. 
This means a list of all error messages logged, and how many times each of them was found, not taking into account the users involved.
They should be sorted by the most common error to the least common error.
regex: r"ERROR: (.+) \(.+\)"

second csv is a usage statistics for the service. 
This means, a list of all users that have used the system including how many info messages and how many error messages they've generated.
This report should be sorted by username.

Format Logs
May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)
Jun  1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)

YYYY_MM_DD_Error_report.csv
errorMessage | Frequency

YYYY_MM_DD_Usage_report.csv
username| frequency info msg | frequency error msg

Use then the csv_ to_html.py script to export the CSV files to HTML and export those

All has to be handled in one script

FWOM QWL
re.search(r"ticky: INFO: ([\w ]*) ", line)
re.search(r"ticky: ERROR: ([\w ]*) ", line)
Sort by keys: sorted(fruit.items(), key=operator.itemgetter(0))
Sort by values: sorted(fruit.items(), key=operator.itemgetter(1))

"""
if __name__ == '__main__':
    placeLog="syslog.log"
    with open(placeLog, "r") as file:
        alllogs = file.readlines()
    logCountErrors = dict()
    logCountUsers=dict()
    for line in alllogs:
        #print(line)
        tempError=re.search(r"ticky: (\w+) (.+) \((.+)\)", line)
        if tempError:
            tempErrorSort=tempError.group(1).strip()
            tempErrorText=tempError.group(2).strip()
            tempErrorUser=tempError.group(3).strip()
            #print(f"Sort: {tempErrorSort}, Text. {tempErrorText}, User: {tempErrorUser}")
            if tempErrorSort=='ERROR':
                #print(f"Error: {tempErrorSort}, Text. {tempErrorText}, User: {tempErrorUser}")
                logCountErrors[tempErrorText]=logCountErrors.get(tempErrorText, 0) +1
                if tempErrorUser in logCountUsers.keys():
                    tempList=logCountUsers.get(tempErrorUser)
                    tempList[1]+=1
                    logCountUsers[tempErrorUser]=tempList
                else:
                    logCountUsers[tempErrorUser]=[0,1]
            elif tempErrorSort=='INFO':
                #print(f"Info: {tempErrorSort}, Text. {tempErrorText}, User: {tempErrorUser}")
                if tempErrorUser in logCountUsers.keys():
                    tempList=logCountUsers.get(tempErrorUser)
                    tempList[0]+=1
                    logCountUsers[tempErrorUser]=tempList
                else:
                    logCountUsers[tempErrorUser]=[1,0]        
            else:
                print('small error')
        else:
            print("BIG ERROR")
    #sort the dictionaries
    sortedLogCountErrors=(sorted(logCountErrors.items(), key=operator.itemgetter(1), reverse=True))
    print(sortedLogCountErrors)
    sortedlogCountUsers=(sorted(logCountUsers.items(), key=operator.itemgetter(0), reverse=False))
    print(sortedlogCountUsers)
    """("Error", "Count") - error_message.csv 
       ("Username", "INFO", "ERROR") - user_statistics.csv"""
    with open('error_message.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Error', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in sortedLogCountErrors:
            writer.writerow({'Error': key, 'Count': value})
    with open('user_statistics.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["Username", "INFO", "ERROR"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in sortedlogCountUsers:
            writer.writerow({'Username': key, 'INFO': value[0], 'ERROR':value[1]})
