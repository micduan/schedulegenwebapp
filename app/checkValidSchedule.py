from operator import itemgetter 
import datetime

def compare_times(lst):
	number_classes = len(lst) / 2

	if number_classes <= 1:
		return True

	start_time = datetime.datetime.strptime(lst[0], '%H:%M')
	end_time = datetime.datetime.strptime(lst[1], '%H:%M')

	index = 2
	while index + 1 <= number_classes * 2:
		current_start_time = datetime.datetime.strptime(lst[index], '%H:%M')
		current_end_time = datetime.datetime.strptime(lst[index + 1], '%H:%M')

		#if one class before the other, it's valid
		if start_time == current_start_time or end_time == current_end_time or (start_time >= current_start_time and start_time <= current_end_time):
			return False

		if (end_time <= current_start_time) or (start_time >= current_end_time):
			index += 2
		else:
			return False

	return True

def check_date( day ):
	#print(lst[:min(len(lst),2)])
	if len(day) <= 2:
		return True
	#if the first time doesn't interfere with any of the other times, check if the second time interferes, etc. etc
	elif compare_times(day):
		return check_date(day[2:])
	else:
		return False
 		
def no_schedule_conflicts( lst ):
	#iterate through each of the days of the week
	for day in range(5):
		if not check_date(lst[day]):
  	 		return False
	return True


def is_valid_schedule( lst ): 
	mon = []
	tues = []
	wed = []
	thurs = []
	fri = []
	length = len(lst)
	# Only check every 4th element (that'll be what day of the week it is)
	index = 0
	while index < length and index != length:
		#sometimes the value returned from the API looks like ['none', 'none', 'none', 'LEC081']

		if lst[index] is None:
			return False

		if 'M' in lst[index]:
			mon.append(lst[index+1])
			mon.append(lst[index+2])
		if 'W' in lst[index]:
			wed.append(lst[index+1])
			wed.append(lst[index+2])						
		if 'F' in lst[index]:
			fri.append(lst[index+1])
			fri.append(lst[index+2])					
		if 'Th' in lst[index]:
			thurs.append(lst[index+1])
			thurs.append(lst[index+2])						
		if 'TT' in lst[index]:
			tues.append(lst[index+1])
			tues.append(lst[index+2])
		if 'T' in lst[index] and 'Th' not in lst[index]:
			tues.append(lst[index+1])
			tues.append(lst[index+2])

		index += 7

	sorted_classes = [mon, tues, wed, thurs, fri]

	return no_schedule_conflicts(sorted_classes)
