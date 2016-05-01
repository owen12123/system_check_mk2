#the goal of this program is to open csv file and analyze all the 
#values to the min and max values which are different in every 
#variable and if there's any value that is out of boundary, report
#which value is out of bound if not give a green sign to car

import csv
import itertools

with open('aa.csv') as csvfile:
	n = 0
	for line in csvfile.readlines():
		n += 1
		if 'ISense 12V 50A' in line:
			#h = line.split(',')
			break
	csvfile.close()
	csvfile = itertools.islice(open('aa.csv'), n-1, None)

#	this method below uses dictreader to contain the column into array

	reader_dict = csv.DictReader(csvfile)
	number = 100.000
	for row in reader_dict:
		print(row['Time'], row['ISense 12V 50A'])
#		break
		if row['Time'] == number:
			print "stop"
			break
	
	#the method below uses reader to put column into list
	reader = csv.reader(csvfile)

#	for line_list in reader:
	
#		if line_list[0] >= number:
#			print 'works#'
#		print line_list[0]
#		pass
#	print line_list[0] +', '+ line_list[1] +', '+ line_list[15]
	