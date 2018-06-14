import app.checkValidSchedule
import pytest

valid = ['2:30', '3:20', '3:30', '4:20']
invalid = ['2:30', '3:20', '2:30', '3:20', '4:30', '5:20']
invalid2 = ['2:30, 3:20', '1:00', '3:00']
valid2 = ['1:00', '5:00']
valid3 = []

def test_valid():
	assert app.checkValidSchedule.check_date(valid) == True

def test_valid2():
	assert app.checkValidSchedule.check_date(valid2) == True

def test_valid3():
	assert app.checkValidSchedule.check_date(valid3) == True

def test_invalid():
	assert app.checkValidSchedule.check_date(invalid) == False