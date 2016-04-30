import csv
with open('aa.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['Format'], row['MoTeC CSV File'], row['Workbook'])
	"""
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print ', '.join(row)
    """