#!/usr/bin/env python3

import os



"""
"""
    

def action_description(filename):
    dict_temp = {}
    with open(filename, 'rb') as opened:
        dict_temp["name"]=opened.readline().rstrip().decode()
        dict_temp["weight"]=int(opened.readline().split()[0])
    print(dict_temp) #debug print
    return_part_body=f"name: {dict_temp['name']}"
    return_part_body+='<br/>'
    return_part_body+=f"weight: {dict_temp['weight']}"
    return_part_body+='<br/><br/>'
    return return_part_body
    

def main():
    source_description = os.path.join(os.path.expanduser("~"), "supplier-data", "descriptions")
    print("Handling in: {}".format(source_description,))
    report_body=""
    for root, directories, files in os.walk(source_description, topdown=False):
        for name in files:
            filename=os.path.join(root, name)
            print("Source: {}".format(filename))
            f, ending_original_file = os.path.splitext(name)
            if ending_original_file == ".txt":
                report_body+=action_description(filename)
    print(report_body)

if __name__ == "__main__":
    main()