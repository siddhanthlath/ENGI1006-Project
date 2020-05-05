#########################################################
# Name : Siddhanth Lath                                 #
# UNI : SLL2200                                         #
#                                                       #
# This file code for my final project to build a html   #
# website using flask and other libraries.              #
#########################################################

#import statements
from flask import Flask, render_template
import requests
import pandas as pd

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/1006")
def page2():
    return render_template("1006.html")

#start the server
if __name__ == "__main__":
    app.run()