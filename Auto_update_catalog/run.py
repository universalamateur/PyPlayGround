#!/usr/bin/env python3

import os
import requests
import json

"""process the text files (001.txt, 003.txt ...) from the supplier-data/descriptions directory.
The script should turn the data into a JSON dictionary by adding all the required fields, 
including the image associated with the fruit (image_name), 
and uploading it to http://[linux-instance-external-IP]/fruits using the Python requests library.

data model in the Django application fruit has the following fields:
 name, weight, description and image_name. 
 The weight field is defined as an integer field. 
 So when you process the weight information of the fruit from the .txt file, you need to convert it into an integer. 
 For example if the weight is "500 lbs", you need to drop "lbs" and convert "500" to an integer.

The image_name field will allow the system to find the image associated with the fruit. 
Don't forget to add all fields, including the image_name! 
The final JSON object should be similar to:
{
    "name": "Watermelon", 
    "weight": 500, 
    "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", 
    "image_name": "010.jpeg"
}

Iterate over all the fruits and use post method from Python requests library to upload all the data to the URL http://[linux-instance-external-IP]/fruits
"""

def upload_description(json_object):
    url = "http://104.154.237.71/fruits/"
    print(url,"  ",json_object)
    payload=json.dumps(json_object)
    print(type(payload))
    response = requests.post(url, data=payload)
    response.raise_for_status()
    #json_filename=str(f)+".json"
    #with open(json_filename,"w") as json_writer:
    #    json.dump(dict_temp, json_writer, indent=4)
    

def create_json(filename):
    dict_temp = {}
    with open(filename, 'rb') as opened:
        dict_temp["name"]=opened.readline().rstrip().decode()
        dict_temp["weight"]=int(opened.readline().split()[0])
        dict_temp["description"]=opened.readline().rstrip().decode()
        f, ending_original_file = os.path.splitext(os.path.basename(filename))
        dict_temp["image_name"]=f+".jpeg"
    #print(dict_temp) #debug print
    json_object_temp = json.dumps(dict_temp)
    #print(json_object_temp) #debug print
    return json_object_temp
    

def main():
    source_description = os.path.join(os.path.expanduser("~"), "supplier-data", "descriptions")
    source_images = os.path.join(os.path.expanduser("~"), "supplier-data", "images")
    print("Handling in: {}  and {}".format(source_description, source_images))
    for root, directories, files in os.walk(source_description, topdown=False):
        for name in files:
            filename=os.path.join(root, name)
            print("Source: {}".format(filename))
            f, ending_original_file = os.path.splitext(name)
            if ending_original_file == ".txt":
                upload_description(create_json(filename))

if __name__ == "__main__":
    main()