import checkvalid
import Check

from uwaterlooapi import UWaterlooAPI
uw = UWaterlooAPI(api_key="095d66cb11782db91d922ab219eccb67")

#determine number of classes in schedule
def schedule():
	num_courses = 0
	if request.form['course1']:
		num_courses = 1
		if request.form['course2']:
			num_courses = 2
			if request.form['course3']:
				num_courses = 3
				if request.form['course4']:
					num_courses = 4
					if request.form['course5']:
						num_courses = 5
						if request.form['course6']:
							num_courses = 6
							if request.form['course7']:
								num_courses = 7

	masterlist = []
	mylist = []
	bool1 = False
	bool2 = False
	bool3 = False
	bool4 = False
	bool5 = False
	bool6 = False
	bool7 = False

	n = request.form['course1']
	m = request.form['course1num']
	dict = uw.course_schedule(n, m)
	total_classes = len(dict)

	if (checkvalid.check_valid(n,m) == False):
		return "courses 1 invalid"

	for x in range(0, total_classes):

		if (num_courses > 1 and bool2 == False):
			bool2 = True
			o = request.form['course2']
			p = request.form['course2num']

			dict2 = uw.course_schedule(o,p)
			total_classes_2 = len(dict2)

			if (checkvalid.check_valid(o,p) == False):
				return 'courses 2 invalid'		

		elif (num_courses > 1):

			for y in range(0, total_classes_2):

				if (num_courses > 2 and bool3 == False):
					bool3 = True
					q = request.form['course3']
					r = request.form['course3num']

					dict3 = uw.course_schedule(q,r)
					total_classes_3 = len(dict3)

					if (checkvalid.check_valid(q,r) == False):
						return 'courses 3 invalid'					

				elif (num_courses > 2):
					for z in range(0, total_classes_3):

						if (num_courses > 3 and bool4 == False):
							bool4 = True
							s = request.form['course4']
							t = request.form['course4num']

							dict4 = uw.course_schedule(s,t)
							total_classes_4 = len(dict4)

							if (checkvalid.check_valid(s,t) == False):
								return 'courses 4 invalid'

						elif (num_courses > 3):
							for a in range(0, total_classes_4):

								if (num_courses > 4 and bool5 == False):
									bool5 = True
									u = request.form['course5']
									v = request.form['course5num']

									dict5 = uw.course_schedule(u,v)
									total_classes_5 = len(dict5)

									if (checkvalid.check_valid(u,v) == False):
										return 'courses 5 invalid'								

								elif (num_courses > 4):
									for b in range(0, total_classes_5):

										if (num_courses > 5 and bool6 == False):
											bool6 = True
											w = request.form['course6']
											xx = request.form['course6num']

											dict6 = uw.course_schedule(w,xx)
											total_classes_6 = len(dict6)

											if (checkvalid.check_valid(w,xx) == False):
												return 'courses 6 invalid'										

										elif (num_courses > 5):
											for c in range(0, total_classes_6):

												if (num_courses > 6 and bool7 == False):
													bool7 = True
													yy = request.form['course7']
													zz = request.form['course7num']

													dict7 = uw.course_schedule(yy,zz)
													total_classes_7 = len(dict7)

													if (checkvalid.check_valid(yy,zz) == False):
														return 'courses 7 invalid'


												elif (num_courses > 6):
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
									
	return str(masterlist)