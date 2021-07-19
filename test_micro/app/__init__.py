from flask import Flask
app = Flask(__name__)
from app import views
#Tried Change for Debug Level for better understanding'
app.config["DEBUG"] = True