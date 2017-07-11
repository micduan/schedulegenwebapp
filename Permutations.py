import checkvalid
import Check

from uwaterlooapi import UWaterlooAPI
uw = UWaterlooAPI(api_key="095d66cb11782db91d922ab219eccb67")


print"How many classes are you taking this term? The maximum number is 7."

while (1):
	num = input()
	if (num <= 7 and num > 0):
		break
	else:
		print"You've inputted an invalid number. Please enter a number less than 7."

def schedule():
	masterlist = []
	mylist = []
	bool1 = False
	bool2 = False
	bool3 = False
	bool4 = False
	bool5 = False
	bool6 = False
	bool7 = False

	print "Please input the first course (e.g. CS)"
	n = raw_input()
	print "Please input the first course number (e.g. 115)"
	m = raw_input()
	print ' '
	dict = uw.course_schedule(n, m)
	total_classes = len(dict)

	if (checkvalid.check_valid(n,m) == False):
		print "Please enter valid inputs."
		print "Please input the first course (e.g. CS)"
		n = raw_input()
		print"Please input the first course number (e.g. 115)"
		m = raw_input()
		print ' '	

	for x in range(0, total_classes):

		if (num > 1 and bool2 == False):
			bool2 = True
			print "Please input the second course"
			o = raw_input()
			print "Please input the second course number"
			p = raw_input()

			dict2 = uw.course_schedule(o,p)
			total_classes_2 = len(dict2)

			if (checkvalid.check_valid(o,p) == False):
				print "Please enter valid inputs."
				print "Please input the second course (e.g. CS)"
				o = raw_input()
				print"Please input the second course number (e.g. 115)"
				p = raw_input()
				print ' '			

		elif (num > 1):

			for y in range(0, total_classes_2):

				if (num > 2 and bool3 == False):
					bool3 = True
					print "Please input the third course"
					q = raw_input()
					print "Please input the third course number"
					r = raw_input()

					dict3 = uw.course_schedule(q,r)
					total_classes_3 = len(dict3)

					if (checkvalid.check_valid(q,r) == False):
						print "Please enter valid inputs."
						print "Please input the third course (e.g. CS)"
						q = raw_input()
						print"Please input the third course number (e.g. 115)"
						r = raw_input()
						print ' '					

				elif (num > 2):
					for z in range(0, total_classes_3):

						if (num > 3 and bool4 == False):
							bool4 = True
							print"Please input the fourth course"
							s = raw_input()
							print"Please input the fourth course number"
							t = raw_input()

							dict4 = uw.course_schedule(s,t)
							total_classes_4 = len(dict4)

							if (checkvalid.check_valid(s,t) == False):
								print "Please enter valid inputs."
								print "Please input the first course (e.g. CS)"
								s = raw_input()
								print"Please input the first course number (e.g. 115)"
								t = raw_input()
								print ' '

						elif (num > 3):
							for a in range(0, total_classes_4):

								if (num > 4 and bool5 == False):
									bool5 = True
									print "Please input the fifth course"
									u = raw_input()
									print "Please input the fifth course number"
									v = raw_input()

									dict5 = uw.course_schedule(u,v)
									total_classes_5 = len(dict5)

									if (checkvalid.check_valid(u,v) == False):
										print "Please enter valid inputs."
										print "Please input the first course (e.g. CS)"
										u = raw_input()
										print"Please input the first course number (e.g. 115)"
										v = raw_input()
										print ' '									

								elif (num > 4):
									for b in range(0, total_classes_5):

										if (num > 5 and bool6 == False):
											bool6 = True
											print"Please input the sixth course"
											w = raw_input()
											print"Please input the sixth course number"
											xx = raw_input()

											dict6 = uw.course_schedule(w,xx)
											total_classes_6 = len(dict6)

											if (checkvalid.check_valid(w,xx) == False):
												print "Please enter valid inputs."
												print "Please input the first course (e.g. CS)"
												w = raw_input()
												print"Please input the first course number (e.g. 115)"
												xx = raw_input()
												print ' '											

										elif (num > 5):
											for c in range(0, total_classes_6):

												if (num > 6 and bool7 == False):
													bool7 = True
													print "Please input the seventh course"
													yy = raw_input()
													print "Please input the seventh course number"
													zz = raw_input()

													dict7 = uw.course_schedule(yy,zz)
													total_classes_7 = len(dict7)

													if (checkvalid.check_valid(yy,zz) == False):
														print "Please enter valid inputs."
														print "Please input the first course (e.g. CS)"
														yy = raw_input()
														print"Please input the first course number (e.g. 115)"
														zz = raw_input()
														print ' '


												elif (num > 6):
													for d in range(0, total_classes_7):


														mylist = [(dict[x]['classes'][0]['date']['weekdays']),
														(dict[x]['classes'][0]['date']['start_time']),
														(dict[x]['classes'][0]['date']['end_time']),
														(dict2[y]['classes'][0]['date']['weekdays']),
														(dict2[y]['classes'][0]['date']['start_time']),
														(dict2[y]['classes'][0]['date']['end_time']),
														(dict3[z]['classes'][0]['date']['weekdays']),
														(dict3[z]['classes'][0]['date']['start_time']),
														(dict3[z]['classes'][0]['date']['end_time']),
														(dict4[a]['classes'][0]['date']['weekdays']),
														(dict4[a]['classes'][0]['date']['start_time']),
														(dict4[a]['classes'][0]['date']['end_time']),
														(dict5[b]['classes'][0]['date']['weekdays']),
														(dict5[b]['classes'][0]['date']['start_time']),
														(dict5[b]['classes'][0]['date']['end_time']),
														(dict6[c]['classes'][0]['date']['weekdays']),
														(dict6[c]['classes'][0]['date']['start_time']),
														(dict6[c]['classes'][0]['date']['end_time']),
														(dict7[d]['classes'][0]['date']['weekdays']),
														(dict7[d]['classes'][0]['date']['start_time']),
														(dict7[d]['classes'][0]['date']['end_time'])]

														if (Check.sort_classes(mylist) == True):
															masterlist.append(mylist)

													d = 0
													c = 0

												else:
													mylist = [(dict[x]['classes'][0]['date']['weekdays']),
													(dict[x]['classes'][0]['date']['start_time']),
													(dict[x]['classes'][0]['date']['end_time']),
													(dict2[y]['classes'][0]['date']['weekdays']),
													(dict2[y]['classes'][0]['date']['start_time']),
													(dict2[y]['classes'][0]['date']['end_time']),
													(dict3[z]['classes'][0]['date']['weekdays']),
													(dict3[z]['classes'][0]['date']['start_time']),
													(dict3[z]['classes'][0]['date']['end_time']),
													(dict4[a]['classes'][0]['date']['weekdays']),
													(dict4[a]['classes'][0]['date']['start_time']),
													(dict4[a]['classes'][0]['date']['end_time']),
													(dict5[b]['classes'][0]['date']['weekdays']),
													(dict5[b]['classes'][0]['date']['start_time']),
													(dict5[b]['classes'][0]['date']['end_time']),
													(dict6[c]['classes'][0]['date']['weekdays']),
													(dict6[c]['classes'][0]['date']['start_time']),
													(dict6[c]['classes'][0]['date']['end_time'])]
											
													if (Check.sort_classes(mylist) == True):
														masterlist.append(mylist)											
											c = 0
											b = 0
											d = 0

										else:
											mylist = [(dict[x]['classes'][0]['date']['weekdays']),
											(dict[x]['classes'][0]['date']['start_time']),
											(dict[x]['classes'][0]['date']['end_time']),
											(dict2[y]['classes'][0]['date']['weekdays']),
											(dict2[y]['classes'][0]['date']['start_time']),
											(dict2[y]['classes'][0]['date']['end_time']),
											(dict3[z]['classes'][0]['date']['weekdays']),
											(dict3[z]['classes'][0]['date']['start_time']),
											(dict3[z]['classes'][0]['date']['end_time']),
											(dict4[a]['classes'][0]['date']['weekdays']),
											(dict4[a]['classes'][0]['date']['start_time']),
											(dict4[a]['classes'][0]['date']['end_time']),
											(dict5[b]['classes'][0]['date']['weekdays']),
											(dict5[b]['classes'][0]['date']['start_time']),
											(dict5[b]['classes'][0]['date']['end_time'])]
											
											if (Check.sort_classes(mylist) == True):
												masterlist.append(mylist)

									c = 0
									b = 0
									d = 0
									a = 0

								else:
									mylist = [(dict[x]['classes'][0]['date']['weekdays']),
									(dict[x]['classes'][0]['date']['start_time']),
									(dict[x]['classes'][0]['date']['end_time']),
									(dict2[y]['classes'][0]['date']['weekdays']),
									(dict2[y]['classes'][0]['date']['start_time']),
									(dict2[y]['classes'][0]['date']['end_time']),
									(dict3[z]['classes'][0]['date']['weekdays']),
									(dict3[z]['classes'][0]['date']['start_time']),
									(dict3[z]['classes'][0]['date']['end_time']),
									(dict4[a]['classes'][0]['date']['weekdays']),
									(dict4[a]['classes'][0]['date']['start_time']),
									(dict4[a]['classes'][0]['date']['end_time'])]	


									if (Check.sort_classes(mylist) == True):
										masterlist.append(mylist)
							a = 0
							b = 0
							c = 0
							d = 0
							z = 0

						else:
							mylist = [(dict[x]['classes'][0]['date']['weekdays']),
							(dict[x]['classes'][0]['date']['start_time']),
							(dict[x]['classes'][0]['date']['end_time']),
							(dict2[y]['classes'][0]['date']['weekdays']),
							(dict2[y]['classes'][0]['date']['start_time']),
							(dict2[y]['classes'][0]['date']['end_time']),
							(dict3[z]['classes'][0]['date']['weekdays']),
							(dict3[z]['classes'][0]['date']['start_time']),
							(dict3[z]['classes'][0]['date']['end_time'])]


							if (Check.sort_classes(mylist) == True):
								masterlist.append(mylist)
					z = 0
					a = 0 
					b = 0
					c = 0
					d = 0
					y = 0

				else:
					mylist = [(dict[x]['classes'][0]['date']['weekdays']),
					(dict[x]['classes'][0]['date']['start_time']),
					(dict[x]['classes'][0]['date']['end_time']),
					(dict2[y]['classes'][0]['date']['weekdays']),
					(dict2[y]['classes'][0]['date']['start_time']),
					(dict2[y]['classes'][0]['date']['end_time'])]

					if (Check.sort_classes(mylist) == True):
						masterlist.append(mylist)

			y = 0
			a = 0
			b = 0 
			c = 0
			d = 0
			z = 0


		else:
			mylist = [(dict[x]['classes'][0]['date']['weekdays']),
			(dict[x]['classes'][0]['date']['start_time']),
			(dict[x]['classes'][0]['date']['end_time'])]

			if (Check.sort_classes(mylist) == True):
				masterlist.append(mylist)
									
	print masterlist
if __name__ == "__main__":
	schedule()
