from flask import Flask, render_template, request
from uwaterlooapi import UWaterlooAPI
from pprint import pprint
import itertools
import Permutation
import checkvalid
import Check
import json
import datetime
import getCourses
from Course import Course

def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i


app = Flask(__name__, template_folder='Templates')

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
    uw = UWaterlooAPI(api_key=request.form['token'])


    #TODO: ENSURE INPUTS ARE PUT IN VALID FORMAT (USE REGEX)
    try :
        no_classes_before = request.form['before_filter']
        no_classes_before_time = datetime.datetime.strptime(no_classes_before, '%H:%M')
    except:
        no_classes_before = None

    try :
        no_classes_after = request.form['after_filter']
        no_classes_after_time = datetime.datetime.strptime(no_classes_after, '%H:%M')
    except:
        no_classes_after = None

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
                days = courses_list[section]['classes'][0]['date']['weekdays']
                start_time = courses_list[section]['classes'][0]['date']['start_time']

                if no_classes_before:
                    start_time_datetime = datetime.datetime.strptime(start_time, '%H:%M')
                    if start_time_datetime < no_classes_before_time:
                        continue

                end_time = courses_list[section]['classes'][0]['date']['end_time']

                if no_classes_after:
                    end_time_datetime = datetime.datetime.strptime(end_time, '%H:%M')
                    if end_time_datetime > no_classes_after_time:
                        continue

                course_type = courses_list[section]['section'] #either LEC, LAB, or TUT
                instructor = str(courses_list[section]['classes'][0]['instructors'])
                lec_section  = [days, start_time, end_time, course_type, instructor]
                lecture_list.append(lec_section)
            if class_type.find("TUT") == 0:
                days = courses_list[section]['classes'][0]['date']['weekdays']
                start_time = courses_list[section]['classes'][0]['date']['start_time']

                if no_classes_before:
                    start_time_datetime = datetime.datetime.strptime(start_time, '%H:%M')
                    if start_time_datetime < no_classes_before_time:
                        continue

                end_time = courses_list[section]['classes'][0]['date']['end_time']

                if no_classes_after:
                    end_time_datetime = datetime.datetime.strptime(end_time, '%H:%M')
                    if end_time_datetime > no_classes_after_time:
                        continue

                course_type = courses_list[section]['section'] #either LEC, LAB, or TUT
                instructor = str(courses_list[section]['classes'][0]['instructors'])
                tut_section = [days, start_time, end_time, course_type, instructor]
                tutorial_list.append(tut_section)
            if class_type.find("LAB") == 0:
                days = courses_list[section]['classes'][0]['date']['weekdays']
                start_time = courses_list[section]['classes'][0]['date']['start_time']

                if no_classes_before:
                    start_time_datetime = datetime.datetime.strptime(start_time, '%H:%M')
                    if start_time_datetime < no_classes_before_time:
                        continue

                end_time = courses_list[section]['classes'][0]['date']['end_time']

                if no_classes_after:
                    end_time_datetime = datetime.datetime.strptime(end_time, '%H:%M')
                    if end_time_datetime > no_classes_after_time:
                        continue

                course_type = courses_list[section]['section'] #either LEC, LAB, or TUT
                instructor = str(courses_list[section]['classes'][0]['instructors'])
                lab_section = [days, start_time, end_time, course_type, instructor]
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

        if (Check.valid_schedule(flattened_list) == False):
            master_list[schedule] = []
        else:
            master_list[schedule] = list(flatten(master_list[schedule]))

    final_list = filter(None, master_list)

    if len(final_list) == 0:
        final_list = "Sorry, there's no possible schedules!"

    actual_final_list = []


    courses = [Course() for i in range(len(final_list))]
    index = 0
    for course_index in courses:
        course_index.fill_dates(final_list[index])
        actual_final_list.append(course_index.convert_course_to_list())
        index += 1
        del course_index

    '''for index in final_list:
        print 'hi'
        course = Course()
        return final_list[0]
        dump(index)
        course.fill_dates(index)
        actual_final_list.append(course)'''

    return render_template("schedule.html", schedule=actual_final_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)