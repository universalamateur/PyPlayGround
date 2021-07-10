#!/usr/bin/env python3

import os
import requests

"""takes the jpeg images from the supplier-data/images directory that you've processed previously and uploads them to the web server fruit catalog.
"""

def upload_image(filename):
    url = "http://localhost/upload/"
    with open(filename, 'rb') as opened:
        print(f"requests.post({url} with {opened}")
        requests.post(url, files={'file': opened})

def main():
    source = os.path.join(os.path.expanduser("~"), "supplier-data", "images")
    print("Handling in: {} ".format(source))
    for root, directories, files in os.walk(source, topdown=False):
        for name in files:
            filename=os.path.join(root, name)
            print("Source: {}".format(filename))
            f, ending_original_file = os.path.splitext(name)
            if ending_original_file == ".jpeg":
                upload_image(filename)

if __name__ == "__main__":
    main()