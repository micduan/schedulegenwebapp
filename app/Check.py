from operator import itemgetter 
from pprint import pprint

import checkvalid
import datetime


def compare_times(lst):
	number_classes = len(lst) / 2
	if number_classes <= 1:
		return True
	start_time = datetime.datetime.strptime(lst[0], '%H:%M')
	end_time = datetime.datetime.strptime(lst[1], '%H:%M')

	index = 2
	while index <= number_classes:
		current_start_time = datetime.datetime.strptime(lst[index], '%H:%M')
		current_end_time = datetime.datetime.strptime(lst[index + 1], '%H:%M')

		#if one class before the other, it's valid
		if (end_time < current_start_time) or (start_time > current_end_time):
			index += 2
		else:
			return False

	return True

def check_combos2( lst ):
	#print(lst[:min(len(lst),2)])
	if len(lst) <= 2:
		return True
	#if the first time doesn't interfere with any of the other times, check if the second time interferes, etc. etc
	elif compare_times(lst):
		return check_combos2(lst[2:])
	else:
		return False
 		
def check_week( lst ):
	#iterate through each of the days of the week
	for num in range(0, 5):
		if not check_combos2(lst[num]):
  	 		return False
	return True


def valid_schedule( lst ): 
	mon = []
	tues = []
	wed = []
	thurs = []
	fri = []
	length = len(lst)
	# Only check every 4th element (that'll be what day of the week it is)
	for x in range(0, length - 3):

		#sometimes the value returned from the API looks like ['none', 'none', 'none', 'LEC081']

		if lst[x] is None:
			return False

		if 'M' in lst[x]:
			mon.append('M')
			mon.append(lst[x+1])
			mon.append(lst[x+2])
		if 'W' in lst[x]:
			wed.append('W')
			wed.append(lst[x+1])
			wed.append(lst[x+2])						
		if 'F' in lst[x]:
			fri.append('F')
			fri.append(lst[x+1])
			fri.append(lst[x+2])					
		if 'Th' in lst[x]:
			thurs.append('Th')
			thurs.append(lst[x+1])
			thurs.append(lst[x+2])						
		if 'TT' in lst[x]:
			tues.append('T')
			tues.append(lst[x+1])
			tues.append(lst[x+2])
		if 'T' in lst[x] and 'Th' not in lst[x]:
			tues.append('T')
			tues.append(lst[x+1])
			tues.append(lst[x+2])
	new_mon = sorted(mon, key=itemgetter(0))
	new_tues = sorted(tues, key=itemgetter(0))
	new_wed = sorted(wed, key=itemgetter(0))
	new_thurs = sorted(thurs, key=itemgetter(0))
	new_fri = sorted(fri, key=itemgetter(0))

	#Get rid of latter half of array to only contain start and end times
	new_mon_length = len(new_mon)
	new_tues_length = len(new_tues)
	new_wed_length = len(new_wed)
	new_thurs_length = len(new_thurs)
	new_fri_length = len(new_fri)

	new_mon = new_mon[:new_mon_length * 2/ 3]
	new_tues = new_tues[:new_tues_length * 2/ 3]
	new_wed = new_wed[:new_wed_length * 2/ 3]
	new_thurs = new_thurs[:new_thurs_length * 2/ 3]
	new_fri = new_fri[:new_fri_length * 2/ 3]


	sorted_classes = []

	sorted_classes.append(new_mon)
	sorted_classes.append(new_tues)
	sorted_classes.append(new_wed)
	sorted_classes.append(new_thurs)
	sorted_classes.append(new_fri)

	return check_week(sorted_classes)
