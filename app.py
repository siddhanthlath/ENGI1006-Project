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

@app.route("/freshman_year")
def freshman_year():
    return render_template("freshman_year.html")

@app.route("/page2")
def page2():
    return render_template("page2.html")

@app.route("/massive_pairplot")
def massive_pairplot():
    return render_template("massive_pairplot.html")

#start the server
if __name__ == "__main__":
    app.run()