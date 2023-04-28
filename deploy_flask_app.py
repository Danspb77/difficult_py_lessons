# rename file !!!!
from flask import Flask

application= Flask(__name__)

@application.route("/")

def index():
    return "HW from flask"


# ------------------------------main--------------
if __name__=="__main__":
    application.run()