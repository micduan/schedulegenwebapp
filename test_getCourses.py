import pytest
import app.getCourses
from uwaterlooapi import UWaterlooAPI

uw_api_key = "1fc3b6c386a6fbe81e12e88ed4e36f4a"

def test_validCourse():
	uw_api = UWaterlooAPI(uw_api_key)
	courses = app.getCourses.generateCourses(uw_api)
	assert len(courses) > 0