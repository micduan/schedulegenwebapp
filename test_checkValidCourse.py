import pytest
import app.checkValidCourse
from uwaterlooapi import UWaterlooAPI

uw_api_key = "1fc3b6c386a6fbe81e12e88ed4e36f4a"

def test_validCourse():
	uw_api = UWaterlooAPI(uw_api_key)
	assert app.checkValidCourse.course_exists('CS', '135', uw_api) == True

def test_invalidCourse():
	uw_api = UWaterlooAPI(uw_api_key)
	assert app.checkValidCourse.course_exists('DOESNT', '135', uw_api) == False