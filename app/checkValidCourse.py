def course_exists(subject, number, uw_api):
	"""
	subject (str): Abbreviation of course name (e.g. CS)
	number (int): Course number
	Returns boolean representing whether or not course is valid
	"""
	courses = uw_api.courses()

	for course in courses:
		if (subject.upper() == course['subject'] and number == course['catalog_number']):
			return True
	return False
