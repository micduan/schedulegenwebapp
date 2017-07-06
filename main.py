from flask import Flask, render_template, request
from uwaterlooapi import UWaterlooAPI


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/token', methods=['POST'])
def token():
    if request.form['password'] != "":
        uw = UWaterlooAPI(api_key=request.form['password'])
        if 'temperature_24hr_min_c' in uw.current_weather():
            return render_template("select.html")
        else:
            return "Invalid API Token"
    else:
        return "No Token"

if __name__ == "__main__":
    app.run(debug=True)