import requests 
import sys 

sub_list = open("dirlist.txt").read()
directories = sub_list.splitlines()

for one_dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{one_dir}.html" 
    r = requests.get(dir_enum)
    if r.status_code==404:
        pass
    else:
        print("Valid directory:" ,dir_enum)
