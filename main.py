from flask import Flask, render_template, request
from uwaterlooapi import UWaterlooAPI
from pprint import pprint
import itertools
import Permutation
import checkvalid
import Check
import json
import getCourses
import Course

def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i

myvar = UWaterlooAPI(api_key="1fc3b6c386a6fbe81e12e88ed4e36f4a")


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

            courses = getCourses.courses(uw)


            if 'temperature_24hr_min_c' in uw.current_weather():
                return render_template("select.html", token=request.form['password'], courses=courses)
            else:
                return "Invalid API Token"
        else:
            return render_template("main.html")

@app.route('/schedule', methods=['POST', 'GET'])
def schedule():
    uw = UWaterlooAPI(api_key="1fc3b6c386a6fbe81e12e88ed4e36f4a")

    num_courses = 0
    for num in range(1,8):
        if request.form['course' + str(num)]:
            num_courses = num

    master_list = []
    individual_list = []

    for course in range(1,num_courses + 1):
        course_name = request.form['course' + str(course)]
        course_number = request.form['course' + str(course) + 'num']
        if not checkvalid.check_valid(course_name,course_number):
            error_message = ''.join([course_name, course_number, " is not a valid course."])
            return render_template("error.html", errormsg = error_message)
        courses_list = uw.course_schedule(course_name, course_number)
        num_sections = len(courses_list)

        course_list = []
        lecture_list = []
        tutorial_list = []
        lab_list = []
        for section in range(0, num_sections):
            class_type = courses_list[section]['section']
            if class_type.find("LEC") == 0:
                lec_section = [(courses_list[section]['classes'][0]['date']['weekdays']),
                (courses_list[section]['classes'][0]['date']['start_time']),
                (courses_list[section]['classes'][0]['date']['end_time']),
                (courses_list[section]['section'])]
                lecture_list.append(lec_section)
            if class_type.find("TUT") == 0:
                tut_section = [(courses_list[section]['classes'][0]['date']['weekdays']),
                (courses_list[section]['classes'][0]['date']['start_time']),
                (courses_list[section]['classes'][0]['date']['end_time']),
                (courses_list[section]['section'])]
                tutorial_list.append(tut_section)
            if class_type.find("LAB") == 0:
                lab_section = [(courses_list[section]['classes'][0]['date']['weekdays']),
                (courses_list[section]['classes'][0]['date']['start_time']),
                (courses_list[section]['classes'][0]['date']['end_time']),
                (courses_list[section]['section'])]
                lab_list.append(lab_section)

        if lecture_list:
            course_list.append(lecture_list)
        if tutorial_list:
            course_list.append(tutorial_list)
        if lab_list:
            course_list.append(lab_list)
        if master_list:
            course_list.append(master_list)

        master_list = list(itertools.product(*course_list))

    for schedule in range(0,len(master_list)):
        try:
            flattened_list = list(flatten(master_list[schedule]))
        except:
            return str(master_list[schedule])

        if (Check.sort_classes(flattened_list) == False):
            master_list[schedule] = []
        else:
            master_list[schedule] = list(flatten(master_list[schedule]))

    final_list = filter(None, master_list)

    if len(final_list) == 0:
        final_list = "Sorry, there's no possible schedules!"

    return render_template("schedule.html", schedule=final_list)


if __name__ == "__main__":
    app.run(debug=True)