import db
import json
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template("signin.html")


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    return render_template("signup.html")

@app.route('/Homepage', methods = ['GET', 'POST'])
def Homepage():
    return render_template("Homepage.html")

@app.route('/contectUs', methods = ['GET', 'POST'])
def contectUs():
    return render_template("contectUs.html")



@app.route('/signin', methods = ['GET', 'POST'])
def signin():
    status, username = db.check_user()

    data = {
        "username": username,
        "status": status
    }

    return json.dumps(data)



@app.route('/register', methods = ['GET', 'POST'])
def register():
    status = db.insert_data()
    return json.dumps(status)


if __name__ == '__main__':
    app.run(debug = True)