from flask import Flask, render_template, request
from uwaterlooapi import UWaterlooAPI


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/token', methods=['POST', 'GET'])
def token():
    if request.method == 'GET':
        return render_template("main.html")
    elif request.method == 'POST':
        if request.form['password'] != "":
            uw = UWaterlooAPI(api_key=request.form['password'])
            if 'temperature_24hr_min_c' in uw.current_weather():
                return render_template("select.html", token=request.form['password'])
            else:
                return "Invalid API Token"
        else:
            return render_template("main.html")

@app.route('/schedule', methods=['POST'])
def schedule():
    courses = request.form['course1'] + " " + request.form['course2'] + " " + request.form['course3'] + " " + request.form['course4'] + " " + request.form['course5'] + " " + request.form['course6'] + " " + request.form['course7'] + "."
    return courses

if __name__ == "__main__":
    app.run(debug=True)