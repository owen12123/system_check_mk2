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

	reader_dict = csv.DictReader(csvfile)
	number = 100
#	for row in reader_dict:
#		print(row['Time'], row['ISense 12V 50A'])
#		break
#		if row['Time'] = number
#			print "stop"
#			break
	

	reader = csv.reader(csvfile)

	for line_list in reader:
		if line_list[0] >= 0:
			print 'works'
		#print line_list[0]
		pass
	print line_list[0] +', '+ line_list[1] +', '+ line_list[15]