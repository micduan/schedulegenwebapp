from flask import Flask, render_template, request
from uwaterlooapi import UWaterlooAPI
import Permutation
import checkvalid
import Check
import json

myvar = UWaterlooAPI(api_key="095d66cb11782db91d922ab219eccb67")


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
    uw = UWaterlooAPI(api_key="095d66cb11782db91d922ab219eccb67")
    num_courses = 0
    if request.form['course1']:
        num_courses = 1
        if request.form['course2']:
            num_courses = 2
            if request.form['course3']:
                num_courses = 3
                if request.form['course4']:
                    num_courses = 4
                    if request.form['course5']:
                        num_courses = 5
                        if request.form['course6']:
                            num_courses = 6
                            if request.form['course7']:
                                num_courses = 7

    masterlist = []
    mylist = []
    bool1 = False
    bool2 = False
    bool3 = False
    bool4 = False
    bool5 = False
    bool6 = False
    bool7 = False

    course_1 = request.form['course1']
    course_1num = request.form['course1num']
    dict = uw.course_schedule(course_1, course_1num)
    total_classes = len(dict)

    if (checkvalid.check_valid(course_1,course_1num) == False):
        return "courses 1 invalid"

    for x in range(0, total_classes):

        if (num_courses > 1 and bool2 == False):
            bool2 = True
            course_2 = request.form['course2']
            course_2num = request.form['course2num']

            dict2 = uw.course_schedule(course_2,course_2num)
            total_classes_2 = len(dict2)

            if (checkvalid.check_valid(course_2,course_2num) == False):
                return 'courses 2 invalid'      

        elif (num_courses > 1):

            for y in range(0, total_classes_2):

                if (num_courses > 2 and bool3 == False):
                    bool3 = True
                    course_3 = request.form['course3']
                    course_3num = request.form['course3num']

                    dict3 = uw.course_schedule(course_3,course_3num)
                    total_classes_3 = len(dict3)

                    if (checkvalid.check_valid(course_3,course_3num) == False):
                        return 'courses 3 invalid'                  

                elif (num_courses > 2):
                    for z in range(0, total_classes_3):

                        if (num_courses > 3 and bool4 == False):
                            bool4 = True
                            course_4 = request.form['course4']
                            course_4num = request.form['course4num']

                            dict4 = uw.course_schedule(course_4,course_4num)
                            total_classes_4 = len(dict4)

                            if (checkvalid.check_valid(course_4,course_4num) == False):
                                return 'courses 4 invalid'

                        elif (num_courses > 3):
                            for a in range(0, total_classes_4):

                                if (num_courses > 4 and bool5 == False):
                                    bool5 = True
                                    course_5 = request.form['course5']
                                    course_5num = request.form['course5num']

                                    dict5 = uw.course_schedule(course_5,course_5num)
                                    total_classes_5 = len(dict5)

                                    if (checkvalid.check_valid(course_5,course_5num) == False):
                                        return 'courses 5 invalid'                              

                                elif (num_courses > 4):
                                    for b in range(0, total_classes_5):

                                        if (num_courses > 5 and bool6 == False):
                                            bool6 = True
                                            course_6 = request.form['course6']
                                            course_6num = request.form['course6num']

                                            dict6 = uw.course_schedule(course_6,course_6num)
                                            total_classes_6 = len(dict6)

                                            if (checkvalid.check_valid(course_6,course_6num) == False):
                                                return 'courses 6 invalid'                                      

                                        elif (num_courses > 5):
                                            for c in range(0, total_classes_6):

                                                if (num_courses > 6 and bool7 == False):
                                                    bool7 = True
                                                    course_7 = request.form['course7']
                                                    course_7num = request.form['course7num']

                                                    dict7 = uw.course_schedule(course_7,course_7num)
                                                    total_classes_7 = len(dict7)

                                                    if (checkvalid.check_valid(course_7,course_7num) == False):
                                                        return 'courses 7 invalid'


                                                elif (num_courses > 6):
                                                    for d in range(0, total_classes_7):

                                                        mylist = [(dict[x]['classes'][0]['date']['weekdays']),
                                                        (dict[x]['classes'][0]['date']['start_time']),
                                                        (dict[x]['classes'][0]['date']['end_time']),
                                                        (dict2[y]['classes'][0]['date']['weekdays']),
                                                        (dict2[y]['classes'][0]['date']['start_time']),
                                                        (dict2[y]['classes'][0]['date']['end_time']),
                                                        (dict3[z]['classes'][0]['date']['weekdays']),
                                                        (dict3[z]['classes'][0]['date']['start_time']),
                                                        (dict3[z]['classes'][0]['date']['end_time']),
                                                        (dict4[a]['classes'][0]['date']['weekdays']),
                                                        (dict4[a]['classes'][0]['date']['start_time']),
                                                        (dict4[a]['classes'][0]['date']['end_time']),
                                                        (dict5[b]['classes'][0]['date']['weekdays']),
                                                        (dict5[b]['classes'][0]['date']['start_time']),
                                                        (dict5[b]['classes'][0]['date']['end_time']),
                                                        (dict6[c]['classes'][0]['date']['weekdays']),
                                                        (dict6[c]['classes'][0]['date']['start_time']),
                                                        (dict6[c]['classes'][0]['date']['end_time']),
                                                        (dict7[d]['classes'][0]['date']['weekdays']),
                                                        (dict7[d]['classes'][0]['date']['start_time']),
                                                        (dict7[d]['classes'][0]['date']['end_time'])]

                                                        if (Check.sort_classes(mylist) == True):
                                                            masterlist.append(mylist)

                                                    d = 0
                                                    c = 0

                                                else:
                                                    mylist = [(dict[x]['classes'][0]['date']['weekdays']),
                                                    (dict[x]['classes'][0]['date']['start_time']),
                                                    (dict[x]['classes'][0]['date']['end_time']),
                                                    (dict2[y]['classes'][0]['date']['weekdays']),
                                                    (dict2[y]['classes'][0]['date']['start_time']),
                                                    (dict2[y]['classes'][0]['date']['end_time']),
                                                    (dict3[z]['classes'][0]['date']['weekdays']),
                                                    (dict3[z]['classes'][0]['date']['start_time']),
                                                    (dict3[z]['classes'][0]['date']['end_time']),
                                                    (dict4[a]['classes'][0]['date']['weekdays']),
                                                    (dict4[a]['classes'][0]['date']['start_time']),
                                                    (dict4[a]['classes'][0]['date']['end_time']),
                                                    (dict5[b]['classes'][0]['date']['weekdays']),
                                                    (dict5[b]['classes'][0]['date']['start_time']),
                                                    (dict5[b]['classes'][0]['date']['end_time']),
                                                    (dict6[c]['classes'][0]['date']['weekdays']),
                                                    (dict6[c]['classes'][0]['date']['start_time']),
                                                    (dict6[c]['classes'][0]['date']['end_time'])]
                                            
                                                    if (Check.sort_classes(mylist) == True):
                                                        masterlist.append(mylist)                                           
                                            c = 0
                                            b = 0
                                            d = 0

                                        else:
                                            mylist = [(dict[x]['classes'][0]['date']['weekdays']),
                                            (dict[x]['classes'][0]['date']['start_time']),
                                            (dict[x]['classes'][0]['date']['end_time']),
                                            (dict2[y]['classes'][0]['date']['weekdays']),
                                            (dict2[y]['classes'][0]['date']['start_time']),
                                            (dict2[y]['classes'][0]['date']['end_time']),
                                            (dict3[z]['classes'][0]['date']['weekdays']),
                                            (dict3[z]['classes'][0]['date']['start_time']),
                                            (dict3[z]['classes'][0]['date']['end_time']),
                                            (dict4[a]['classes'][0]['date']['weekdays']),
                                            (dict4[a]['classes'][0]['date']['start_time']),
                                            (dict4[a]['classes'][0]['date']['end_time']),
                                            (dict5[b]['classes'][0]['date']['weekdays']),
                                            (dict5[b]['classes'][0]['date']['start_time']),
                                            (dict5[b]['classes'][0]['date']['end_time'])]
                                            
                                            if (Check.sort_classes(mylist) == True):
                                                masterlist.append(mylist)

                                    c = 0
                                    b = 0
                                    d = 0
                                    a = 0

                                else:
                                    mylist = [(dict[x]['classes'][0]['date']['weekdays']),
                                    (dict[x]['classes'][0]['date']['start_time']),
                                    (dict[x]['classes'][0]['date']['end_time']),
                                    (dict2[y]['classes'][0]['date']['weekdays']),
                                    (dict2[y]['classes'][0]['date']['start_time']),
                                    (dict2[y]['classes'][0]['date']['end_time']),
                                    (dict3[z]['classes'][0]['date']['weekdays']),
                                    (dict3[z]['classes'][0]['date']['start_time']),
                                    (dict3[z]['classes'][0]['date']['end_time']),
                                    (dict4[a]['classes'][0]['date']['weekdays']),
                                    (dict4[a]['classes'][0]['date']['start_time']),
                                    (dict4[a]['classes'][0]['date']['end_time'])]   


                                    if (Check.sort_classes(mylist) == True):
                                        masterlist.append(mylist)
                            a = 0
                            b = 0
                            c = 0
                            d = 0
                            z = 0

                        else:
                            mylist = [(dict[x]['classes'][0]['date']['weekdays']),
                            (dict[x]['classes'][0]['date']['start_time']),
                            (dict[x]['classes'][0]['date']['end_time']),
                            (dict2[y]['classes'][0]['date']['weekdays']),
                            (dict2[y]['classes'][0]['date']['start_time']),
                            (dict2[y]['classes'][0]['date']['end_time']),
                            (dict3[z]['classes'][0]['date']['weekdays']),
                            (dict3[z]['classes'][0]['date']['start_time']),
                            (dict3[z]['classes'][0]['date']['end_time'])]

                            try:
                                if (Check.sort_classes(mylist) == True):
                                    masterlist.append(mylist)
                            except:
                                return str(mylist)
                    z = 0
                    a = 0 
                    b = 0
                    c = 0
                    d = 0
                    y = 0

                else:
                    mylist = [(dict[x]['classes'][0]['date']['weekdays']),
                    (dict[x]['classes'][0]['date']['start_time']),
                    (dict[x]['classes'][0]['date']['end_time']),
                    (dict2[y]['classes'][0]['date']['weekdays']),
                    (dict2[y]['classes'][0]['date']['start_time']),
                    (dict2[y]['classes'][0]['date']['end_time'])]

                    if (Check.sort_classes(mylist) == True):
                        masterlist.append(mylist)

            y = 0
            a = 0
            b = 0 
            c = 0
            d = 0
            z = 0


        else:
            mylist = [(dict[x]['classes'][0]['date']['weekdays']),
            (dict[x]['classes'][0]['date']['start_time']),
            (dict[x]['classes'][0]['date']['end_time'])]

            if (Check.sort_classes(mylist) == True):
                masterlist.append(mylist)
                     
    return render_template("schedule.html", schedule=masterlist)
#def schedule():
#    return render_template("schedule.html", token=request.form['password'], course1=request.form['course1'], course2=request.form['course2'], 
#        course3=request.form['course3'], course4=request.form['course4'], course5=request.form['course5'], course6=request.form['course6'],
#        course7=request.form['course7'])


if __name__ == "__main__":
    app.run(debug=True)