#!/usr/bin/env python3


import csv
import datetime
import requests
import pprint


FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"


def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    temp_list_employees=[]
    dictStartEmployee={}
    for line in response.iter_lines():
        split_line=line.decode("UTF-8").split(',')
        #print(split_line)
        temp_list_employees.append([split_line[0],split_line[1], split_line[3].split("-")])
    temp_list_employees.pop(0)
    #print(temp_list_employees)
    for elem in temp_list_employees:
        if elem[2][0] in dictStartEmployee.keys():
            if elem[2][1] in dictStartEmployee[elem[2][0]].keys():
                if elem[2][2] in dictStartEmployee[elem[2][0]][elem[2][1]].keys():
                    dictStartEmployee[elem[2][0]][elem[2][1]][elem[2][2]].append(str(elem[0] + ' ' + elem[1]))
                else:
                    dictStartEmployee[elem[2][0]][elem[2][1]][elem[2][2]]=[str(elem[0] + ' ' + elem[1])]
            else:
                dictStartEmployee[elem[2][0]][elem[2][1]] = {}
                dictStartEmployee[elem[2][0]][elem[2][1]][elem[2][2]]=[str(elem[0] + ' ' + elem[1])]
        else:
            dictStartEmployee[elem[2][0]] = {}
            dictStartEmployee[elem[2][0]][elem[2][1]] = {}
            dictStartEmployee[elem[2][0]][elem[2][1]][elem[2][2]]=[str(elem[0] + ' ' + elem[1])]       
    #pprint.pprint(dictStartEmployee)            
    return dictStartEmployee

def main():
    start_date = get_start_date() #datetime.datetime(2018, 1, 1) #
    #print(start_date)
    dictDateEmployee={}
    dictDateEmployee=get_file_lines(FILE_URL)
    #pprint.pprint(dictDateEmployee)
    #list_newer(start_date, dictDateEmployee)
    start_year = start_date.year
    stop_year = datetime.date.today().year
    start_month = start_date.month
    stop_month = datetime.date.today().month
    start_day = start_date.day
    stop_day = datetime.date.today().day
    #print(f"{start_year} - {start_month} - {start_day}")
    #print(f"{stop_year} - {stop_month} - {stop_day}")
    while(start_year<stop_year or (start_year<=stop_year and start_month<stop_month) or( start_year<=stop_year and start_month<stop_month and start_day<=stop_day)):
        #print(f"{start_year} - {start_month} - {start_day}")
        start_year_string=str(start_year)
        start_month_string=str(start_month).zfill(2)
        start_day_string=str(start_day).zfill(2)
        if start_year_string in dictDateEmployee.keys():
            #print(f"{start_year}")
            if start_month_string in dictDateEmployee[start_year_string].keys():
                #print(f"{start_year} - {start_month}")
                if start_day_string in dictDateEmployee[start_year_string][start_month_string].keys():
                    #print(f"{start_year} - {start_month} - {start_day}")
                    for elem in dictDateEmployee[start_year_string][start_month_string][start_day_string]:
                            print_date=datetime.datetime(start_year, start_month, start_day)
                            print("Started on {}: {}".format(print_date.strftime("%b %d, %Y"), elem))
        if start_day<31:
            start_day+=1
        elif start_month<12:
            start_day=1
            start_month+=1
        elif start_year<stop_year:
            start_day=1
            start_month=1
            start_year+=1
        else:
            break


if __name__ == "__main__":
    main()

