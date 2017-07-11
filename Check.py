from operator import itemgetter 

import checkvalid


def compare_two( lstA, lstB ):
	#print((((lstA[1]) < (lstB[1])) and ((lstA[2]) < (lstB[1]))))
	return (((lstA[1]) < (lstB[1])) and ((lstA[2]) < (lstB[1])))

def check_combos2( lst ):
	#print(lst[:min(len(lst),2)])
	if len(lst) <= 3:
		#print("True")
		return True
	elif compare_two(lst[0], lst[1]):
		return check_combos2(lst[1:])
	else:
		#print("False")
		return False
 		
def check_week( lst ):
	x = 0
	tof = True
	for num in range(0, len(lst)):
		if check_combos2(lst[x]):
	 		x = x+1
		else:
  	 		tof = False
  	 		break
	return tof


def sort_classes( lst ): 
	mon = []
	tues = []
	wed = []
	thurs = []
	fri = []
	length = len(lst)
	for x in range(0, length):
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

	sorted_classes = []

	sorted_classes.append(new_mon)
	sorted_classes.append(new_tues)
	sorted_classes.append(new_wed)
	sorted_classes.append(new_thurs)
	sorted_classes.append(new_fri)

	return check_week(sorted_classes)
