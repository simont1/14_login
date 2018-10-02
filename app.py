#Box2 - Anton Danylenko, Simon Tsui
#SoftDev1 pd8
#K14 -- Do I know you?
#2018-10-01

from flask import Flask
from flask import session
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect

login_info = {"addis": "ababa"}
usr_input = {}
app = Flask(__name__)
@app.route("/")
def start():
    return render_template("login.html")


@app.route("/auth", methods = ['GET'])
def authenticate():
    print(url_for('authenticate'))
    usr_input["Username"] = request.args["Username"]
    usr_input["Password"] = request.args["Password"]
    if (request.args['Username'] == 'addis' and request.args['Password'] == 'ababa'):
        return redirect(url_for("success"))
    else:
        return redirect(url_for('display_login'))

@app.route("/again")
def display_login():
    if(usr_input["Username"] != "addis" and usr_input["Password"] != "ababa"):
        return render_template("failed.html", a  = "Username and Password ")
    elif(usr_input["Username"] != "addis"):
        return render_template("failed.html", a = "Username")
    else:
        return render_template("failed.html", a = "Password")

@app.route("/display_login")
def success():
    print(request.args)
    # return render_template("auth.html", a = request.args['Username'])
    return render_template("auth.html", a = usr_input["Username"])


if __name__ == "__main__":
    app.debug = True
    app.run()
