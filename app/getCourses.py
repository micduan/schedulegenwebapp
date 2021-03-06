def generateCourses(uw_api):
	"""
	api: instance of uwaterloo API
	returns a list of all courses the school is offering
	"""
	uwaterloocourses = uw_api.courses()
	courses = []

	for index in range(0, len(uwaterloocourses)):
		if not (uwaterloocourses[index]['subject'] in courses):
			courses.append(uwaterloocourses[index]['subject'])

	return courses