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
    return render_template("main_page.html")

@app.route("/page1")
def page1():
    return render_template("page1.html")

@app.route("/page2")
def page2():
    return render_template("page2.html")

@app.route("/page3")
def page3():
    return render_template("page3.html")

#start the server
if __name__ == "__main__":
    app.run()