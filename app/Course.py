class Course:
	time_830 = {}
	time_900 = {}
	time_930 = {}
	time_1000 = {}
	time_1030 = {}
	time_1100 = {}
	time_1130 = {}
	time_1200 = {}
	time_1230 = {}
	time_1300 = {}
	time_1330 = {}
	time_1400 = {}
	time_1430 = {}
	time_1500 = {}
	time_1530 = {}
	time_1600 = {}
	time_1630 = {}
	time_1700 = {}
	time_1730 = {}
	time_1800 = {}
	time_1830 = {}
	time_1900 = {}
	time_1930 = {}
	time_2000 = {}
	time_2030 = {}
	time_2100 = {}
	time_2130 = {}
	time_2200 = {}


	def __init__(self):
		self.time_830 = {'time' : '8:30'}
		self.time_900 = {'time' : '9:00'}
		self.time_930 = {'time' : '9:30'}
		self.time_1000 = {'time' : '10:00'}
		self.time_1030 = {'time' : '10:30'}
		self.time_1100 = {'time' : '11:00'}
		self.time_1130 = {'time' : '11:30'}
		self.time_1200 = {'time' : '12:00'}
		self.time_1230 = {'time' : '12:30'}
		self.time_1300 = {'time' : '13:00'}
		self.time_1330 = {'time' : '13:30'}
		self.time_1400 = {'time' : '14:00'}
		self.time_1430 = {'time' : '14:30'}
		self.time_1500 = {'time' : '15:00'}
		self.time_1530 = {'time' : '15:30'}
		self.time_1600 = {'time' : '16:00'}
		self.time_1630 = {'time' : '16:30'}
		self.time_1700 = {'time' : '17:00'}
		self.time_1730 = {'time' : '17:30'}
		self.time_1800 = {'time' : '18:00'}
		self.time_1830 = {'time' : '18:30'}
		self.time_1900 = {'time' : '19:00'}
		self.time_1930 = {'time' : '19:30'}
		self.time_2000 = {'time' : '20:00'}
		self.time_2030 = {'time' : '20:30'}
		self.time_2100 = {'time' : '21:00'}
		self.time_2130 = {'time' : '21:30'}
		self.time_2200 = {'time' : '22:00'}

	def fill_dates(self, lst):
		"""
		Takes list representing a schedule, and parses them to determine what blocks are in use in the schedule
		"""

		length = len(lst)
		index = 0
		while index < length and index != length:

			#sometimes the value returned from the API looks like [u'MWF', u'8:30', u'9:20', u'LEC081']

			if lst[index] is None:
				continue

			start_time = lst[index + 1].replace(":", "")
			end_time = lst[index + 2].replace(":", "")
			instructor = lst[index + 4]


			if 'M' in lst[index]:
				self.add_to_schedule('M', start_time, end_time, instructor)
			if 'W' in lst[index]:
				self.add_to_schedule('W', start_time, end_time, instructor)	
			if 'F' in lst[index]:
				self.add_to_schedule('F', start_time, end_time, instructor)
			if 'Th' in lst[index]:
				self.add_to_schedule('Th', start_time, end_time, instructor)
			if 'TT' in lst[index]:
				self.add_to_schedule('T', start_time, end_time, instructor)
			if 'T' in lst[index] and 'Th' not in lst[index]:
				self.add_to_schedule('T', start_time, end_time, instructor)

			index += 5

	def add_to_schedule(self, date, start_time, end_time, instructor):
		"""
		date: string abbreviation of day of week (Monday through Friday)
		start_time: time class starts, in unicode (e.g. 8:30)
		end_time: time class ends, in unicode (e.g. 9:20)

		"""

		start_time_int = int(start_time.encode('ascii', 'ignore'))
		end_time_int = int(end_time.encode('ascii', 'ignore'))
		time_blocks = self.get_times_used(start_time_int, end_time_int)

		if time_blocks is None:
			return

		response = [True, instructor]

		for time in time_blocks:
			if time == 830:
				self.time_830[date] = response
			if time == 900:
				self.time_900[date] = response
			if time == 930:
				self.time_930[date] = response
			if time == 1000:
				self.time_1000[date] = response
			if time == 1030:
				self.time_1030[date] = response
			if time == 1100:
				self.time_1100[date] = response
			if time == 1130:
				self.time_1130[date] = response
			if time == 1200:
				self.time_1200[date] = response
			if time == 1230:
				self.time_1230[date] = response
			if time == 1300:
				self.time_1300[date] = response
			if time == 1330:
				self.time_1330[date] = response
			if time == 1400:
				self.time_1400[date] = response
			if time == 1430:
				self.time_1430[date] = response
			if time == 1500:
				self.time_1500[date] = response
			if time == 1530:
				self.time_1530[date] = response
			if time == 1600:
				self.time_1600[date] = response
			if time == 1630:
				self.time_1630[date] = response
			if time == 1700:
				self.time_1700[date] = response
			if time == 1730:
				self.time_1730[date] = response
			if time == 1800:
				self.time_1800[date] = response
			if time == 1830:
				self.time_1830[date] = response
			if time == 1900:
				self.time_1900[date] = response
			if time == 1930:
				self.time_1930[date] = response
			if time == 2000:
				self.time_2000[date] = response
			if time == 2030:
				self.time_2030[date] = response
			if time == 2100:
				self.time_2100[date] = response
			if time == 2130:
				self.time_2130[date] = response
			if time == 2200:
				self.time_200[date] = response

	def get_times_used(self, start_time, end_time):
		"""
		start_time (int) : represents time course starts
		end_time (int) : represents time course ends
		returns a list of all course blocks used (e.g. from 8:30 - 9:20, 8:30 - 9:00 are used, and 9:00 - 9:30 are used)
		"""
		current_number = start_time
		times = []
		while current_number < end_time + 1:
			minute = current_number % 100
			if (minute % 30 == 0) and (minute < 60):
				times.append(current_number)
			if minute == 59:
				current_number += 41
			else:
				current_number += 1

		return times

	def convert_course_to_list(self):
		"""
		Returns list which contains all property's dates
		"""
		return list([
			self.time_830,
			self.time_900,
			self.time_930,
			self.time_1000,
			self.time_1030,
			self.time_1100,
			self.time_1130,
			self.time_1200,
			self.time_1230,
			self.time_1300,
			self.time_1330,
			self.time_1400,
			self.time_1430,
			self.time_1500,
			self.time_1530,
			self.time_1600,
			self.time_1630,
			self.time_1700,
			self.time_1730,
			self.time_1800,
			self.time_1830,
			self.time_1900,
			self.time_1930,
			self.time_2000,
			self.time_2030,
			self.time_2100,
			self.time_2130,
			self.time_2200
		])