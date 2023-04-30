# rename file !!!!
from flask import Flask

application= Flask(__name__)

@application.route("/")

def index():
    return "<font color=blue>HW from flask</font>"


@application.route("/helppage")

def helppage():
    return "<b>Message form heplpage </b>"


@application.route("/user/<username>")

def username_page(username):
    return " Hello " + username.upper()


@application.route("/path/<path:subpath>")

def print_subpath(subpath):
    return "Subpath is " + subpath


@application.route("/squaring/<int:x>")

def squaring(x):
    return "Squaring from " + str(x)+ " is " + str(x*x)


@application.route("/htmlpage")

def htmlpage():
    file=open("name...",mode='r')
    page=file.read()
    file.close()
    return page






# ------------------------------main--------------
if __name__=="__main__":

    application.debug=True
    application.env="working hard"
    application.run()