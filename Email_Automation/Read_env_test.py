#!/usr/bin/env python3

import os
from dotenv import load_dotenv

"""Test to read values out of an .env file"""

def main():
    load_dotenv()
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    SMTP_PORT = os.getenv("SMTP_PORT")
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASS  = os.getenv("SMTP_PASS")
    SMTP_SENDER  = os.getenv("SMTP_SENDER")
    SMTP_RECP  = os.getenv("SMTP_RECP")
    print(f"SMTP_SERVER : {SMTP_SERVER}")
    print(f"SMTP_PORT : {SMTP_PORT}")
    print(f"SMTP_USER : {SMTP_USER}")
    print(f"SMTP_PASS : {SMTP_PASS}")
    print(f"SMTP_SENDER : {SMTP_SENDER}")
    print(f"SMTP_RECP : {SMTP_RECP}")

 

if __name__ == "__main__":
    main()