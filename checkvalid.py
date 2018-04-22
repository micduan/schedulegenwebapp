from uwaterlooapi import UWaterlooAPI
uw = UWaterlooAPI(api_key="095d66cb11782db91d922ab219eccb67")

def check_valid(subject, number):
	courses = uw.courses()
	length = len(courses)

<<<<<<< HEAD
	for course in range(0,length):
		if (subject == courses[course]['subject'] and number == courses[course]['catalog_number']):
=======
	for a in range(0,length):
		if (subject == courses[a]['subject'] and number == courses[a]['catalog_number']):
>>>>>>> 5c44ad5c1889d5f1a5697169538f852c5d8334b4
			return True
	return False
