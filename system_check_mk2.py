import csv
import itertools

with open('aa.csv') as csvfile:
	n = 0
	for line in csvfile.readlines():
		n += 1
		if 'ISense 12V 50A' in line:
			h = line.split(',')
			break
	csvfile.close()
	csvfile = itertools.islice(open('aa.csv'), n-1, None)

	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['Time'], row['ISense 12V 50A'])
	"""
	This is for read all the file-not very useful
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print ', '.join(row)
    """