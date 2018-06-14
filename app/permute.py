from uwaterlooapi import UWaterlooAPI
import datetime
import checkValidCourse
import checkValidSchedule
import itertools

def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i

def generateSchedules(request):
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

    try:
        if request.form['tutorials']:
            tutorials_active = False
        else:
            tutorials_active = True

    except:
        tutorials_active = True

    num_courses = 0
    for num in range(1,8):
        if request.form['course' + str(num)]:
            num_courses = num

    master_list = []

    for course in range(1,num_courses + 1):
        course_name = request.form['course' + str(course)]
        course_number = request.form['course' + str(course) + 'num']
        course_title = course_name + " " + course_number
        if not checkValidCourse.course_exists(course_name,course_number, uw):
            error_message = ''.join([course_name, course_number, " is not a valid course."])
            return [False, error_message]
        courses_list = uw.course_schedule(course_name, course_number)
        num_sections = len(courses_list)

        course_list = []
        lecture_list = []
        tutorial_list = []
        lab_list = []

        for section in range(0, num_sections):
            class_type = courses_list[section]['section']
            if class_type.find("LEC") == 0 or class_type.find("TUT") == 0 or class_type.find("LAB") == 0:
                days = courses_list[section]['classes'][0]['date']['weekdays']
                start_time = courses_list[section]['classes'][0]['date']['start_time']
                section_number = courses_list[section]['section']

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
                instructor = courses_list[section]['classes'][0]['instructors']

                if instructor:
                    instructor = str(instructor[0].encode('ascii', 'ignore'))
                else:
                    instructor = 'None'


            if class_type.find("LEC") == 0:
                lec_section  = [days, start_time, end_time, course_type, instructor, course_title, section_number]
                lecture_list.append(lec_section)
            if class_type.find("TUT") == 0 and tutorials_active:
                tut_section = [days, start_time, end_time, course_type, instructor, course_title, section_number]
                tutorial_list.append(tut_section)
            if class_type.find("LAB") == 0:
                lab_section = [days, start_time, end_time, course_type, instructor, course_title, section_number]
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
            return False

        if (not checkValidSchedule.is_valid_schedule(flattened_list)):
            master_list[schedule] = []
        else:
            master_list[schedule] = flattened_list

    final_list = filter(None, master_list)

    return final_list