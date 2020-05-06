#########################################################
# Name : Siddhanth Lath                                 #
# UNI : SLL2200                                         #
#                                                       #
# This file code for my final project to build a html   #
# website using flask and other libraries.              #
#########################################################

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def main_page():
    return render_template("main_page.html")

@app.route("/freshman_year")
def freshman_year():
    return render_template("freshman_year.html")

@app.route("/my_vlogs")
def my_vlogs():
    return render_template("my_vlogs.html")

@app.route("/massive_pairplot")
def massive_pairplot():
    return render_template("massive_pairplot.html")

#start the server
if __name__ == "__main__":
    app.run()