#!/usr/bin/env python3

import os
from email.message import EmailMessage
import mimetypes
import smtplib
from dotenv import load_dotenv
import datetime
import getpass

"""Write a script that summarizes and processes sales data into different categories
Generate a PDF using Python
Automatically send a PDF by email"""

def main():
    source = os.path.join(os.path.expanduser("~"), "data") #USer home plus path
    #source os.path.abspath(os.path.join(os.sep, "data", "input")) #absolute path linux beginning with root
    attachement_path=(os.path.join(source, "exmple.png"))
    #print(attachement_path) #Debug Print
    mime_type, _ =mimetypes.guess_type(attachement_path)
    #print(mime_type) #Debug Print
    mime_type, mime_subtype = mime_type.split('/', 1)


if __name__ == "__main__":
    main()