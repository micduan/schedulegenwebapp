from uwaterlooapi import UWaterlooAPI
uw = UWaterlooAPI(api_key="095d66cb11782db91d922ab219eccb67")

def check_valid(subject, number):
	"""
	subject (str): Abbreviation of course name (e.g. CS)
	number (int): Course number
	Returns boolean representing whether or not course is valid
	"""
	courses = uw.courses()
	length = len(courses)

	for course in range(0,length):
		if (subject == courses[course]['subject'] and number == courses[course]['catalog_number']):
			return True
	return False
