#!/usr/bin/env python3

import os
import requests

def run_Files(folder):
    return_list=[]
    for root, directories, files in os.walk(folder, topdown=False):
        for name in files:
            filename=os.path.join(root, name)
            print("Source: {}".format(filename))
            temp_dict={}
            with open(filename) as f:
                temp_dict["title"]=f.readline().rstrip('\n')
                temp_dict["name"]=f.readline().rstrip('\n')
                temp_dict["date"]=f.readline().rstrip('\n')
                temp_dict["feedback"]=f.readline().rstrip('\n')
            return_list.append(temp_dict)
    return return_list

def push_files(list_of_feedback):
    #headers_request= {'Content-type': 'application/json; charset=UTF-8'}
    url="http://34.136.200.71/feedback/"
    for elem in list_of_feedback:
        payload=elem
        response = requests.post(url, data=payload , verify=False, timeout=10)#, headers=headers_request)
        response.raise_for_status()


def main():
    source = os.path.abspath(os.path.join(os.sep, "data", "feedback"))
    feedback_list=[]
    feedback_list=run_Files(source)
    print(feedback_list)
    push_files(feedback_list)



if __name__ == "__main__":
    main()