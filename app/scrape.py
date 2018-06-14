from selenium import webdriver
import math
import time
import MySQLdb

def getRatings():

	#db = MySQLdb.connect(host="db",
	#	user="root",
	#	passwd="password",
	#	db="ratemyprof",
	#	port=3306)

	#cursor = db.cursor()

	options = webdriver.ChromeOptions()
	options.binary_location= "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome";
	chrome_driver_binary = "/users/micduan/documents/sideprojects/schedulegenwebapp-master/app/chromedriver"
	driver = webdriver.Chrome(executable_path=chrome_driver_binary, chrome_options=options)

	starturl = "http://www.ratemyprofessors.com/search.jsp?queryBy=schoolId&schoolName=University+of+Waterloo&schoolID=1490&queryoption=TEACHER"
	driver.get(starturl)

	num_ratings = driver.find_element_by_xpath('//span[@class = "professor-count"]').text
	num_pages = int(math.ceil(int(num_ratings)/20)) - 1

	for i in range(num_pages):
		button = driver.find_element_by_xpath('//div[@class = "content"]')
		driver.execute_script("arguments[0].click();", button)


	prof_urls = []
	profs = driver.find_elements_by_xpath('//div[@class = "result-list"]//a')

	for prof in profs:
		driver.execute_script("arguments[0].scrollIntoView();", prof)
		if "ShowRatings" in prof.get_attribute("href"):
			prof_urls.append(prof.get_attribute("href"))

	for url in prof_urls:
		driver.get(url)
		firstname = driver.find_element_by_xpath('//span[@class = "pfname"]').text
		lastname = driver.find_element_by_xpath('//span[@class = "plname"]').text
		rating = float(driver.find_element_by_xpath('//div[@class = "grade"]').text)
		prof_num_ratings = int(driver.find_element_by_xpath('//div[@data-table = "rating-filter"]').text.split(" ")[0])
		print firstname + " " + lastname + " " + str(rating) + " " + str(prof_num_ratings)
		#sql = """INSERT INTO professors(first, last, rating, num_ratings)
		#			VALUES(%s, %s, %s, %s)"""
		#cursor.execute("""INSERT INTO professors(first, last, rating, num_ratings) VALUES(%s, %s, %s, %s)""", (firstname, lastname, rating, prof_num_ratings))
		#db.commit()

	#db.close()
	print num_pages

if __name__ == '__main__':
	getRatings() 