from uwaterlooapi import UWaterlooAPI

def courses(api):
	uwaterloocourses = api.courses()

	courses = []

	for index in range(0, len(uwaterloocourses)):
		if not (uwaterloocourses[index]['subject'] in courses):
			courses.append(uwaterloocourses[index]['subject'])

	return courses