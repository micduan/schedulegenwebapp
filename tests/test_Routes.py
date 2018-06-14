import flask
from flask import request
import re
import os
import tempfile
import requests
import unittest

app = flask.Flask(__name__)

def test_index():
	with app.test_request_context('/'):
		assert flask.request.path == '/'

def test_users():
	with app.test_request_context('/users'):
		assert flask.request.path == '/users'

class TestFlask(unittest.TestCase):

	def test_web_app_running(self):
		try:
			r = requests.get("http://127.0.0.1:5000/")
			self.assertEquals(r.status_code, 200)
		except:
			self.fail("Could not open web app.")

	def test_home_loaded_propertly(self):
		r = requests.get("http://127.0.0.1:5000/")
		text_on_page = r.text
		self.assertGreaterEqual(text_on_page.find('Schedule'), 0)

	def test_saved_schedules_not_logged_in(self):
		r = requests.get("http://127.0.0.1:5000/saved/")
		self.assertEquals(r.status_code, 404)

	def test_token_get(self):
		r = requests.get("http://127.0.0.1:5000/token")
		text_on_page = r.text
		self.assertEquals(r.status_code, 200)

	def test_token_get_text(self):
		r = requests.get("http://127.0.0.1:5000/token")
		text_on_page = r.text
		self.assertGreaterEqual(text_on_page.find('Please proceed'), 0)

	def test_login(self):
		r = requests.post("http://127.0.0.1:5000/login",
			data={'username': 'micduan', 'password': '7fedrah'})
		self.assertEquals(r.status_code, 200)

	def test_user_required_pages(self):
		session = requests.Session()
		session.post("http://127.0.0.1:5000/login",
			data={'username': 'micduan', 'password': '7fedrah'})
		r = session.get("http://127.0.0.1:5000/saved")
		self.assertEquals(r.status_code, 200)

		text_on_page = r.text
		self.assertGreaterEqual(text_on_page.find('COMING SOON'), 0)

	def test_user_required_pages_text(self):
		session = requests.Session()
		session.post("http://127.0.0.1:5000/login",
			data={'username': 'micduan', 'password': '7fedrah'})
		r = session.get("http://127.0.0.1:5000/saved")
		text_on_page = r.text
		self.assertGreaterEqual(text_on_page.find('COMING SOON'), 0)

	#def test_register_user(self):

	#def test_admin_pages(self):

	#def test_valid_schedule(self):

	#def test_invalid_schedule(self):

if __name__ == '__main__':
    unittest.main()