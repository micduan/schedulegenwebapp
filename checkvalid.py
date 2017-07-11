from uwaterlooapi import UWaterlooAPI
uw = UWaterlooAPI(api_key="095d66cb11782db91d922ab219eccb67")

def check_valid(subject, number):
	courses = uw.courses()
	length = len(courses)

	for a in range(0,length):
		if (subject == courses[a]['subject'] and number == courses[a]['catalog_number']):
			return True
	return False
