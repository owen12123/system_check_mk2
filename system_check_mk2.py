import csv
import itertools

with open('aa.csv') as csvfile:
	n = 0
	for line in csvfile.readlines():
		n += 1
		if 'Wheel Speed FR' and 'ISense 12V 50A' in line:
			h = line.split(',')
			break
	csvfile.close()
	csvfile = itertools.islice(open('aa.csv'), n-1, None)

	reader = csv.reader(csvfile)

	for line_list in reader:
		pass
	print line_list[0]
	print line_list[1]
	print line_list[15]

'''
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['Time'], row['ISense 12V 50A'], row['BR2 Valid Receptions'])
'''