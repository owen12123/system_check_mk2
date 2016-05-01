#the goal of this program is to open csv file and analyze all the 
#values to the min and max values which are different in every 
#variable and if there's any value that is out of boundary, report
#which value is out of bound if not give a green sign to car

import csv
import itertools

#data compare method

def compare_num(a, max, min):
if a>max:
	return false
elif a<min:
	return false
else:
	return true

#question: is it better if we make a separate class and
#store all the data in that class? or make a hashtable?
#or build a csv file and import these data from it and compare 

with open('aa.csv') as csvfile:
	n = 0
	for line in csvfile.readlines():
		n += 1
		if 'ISense 12V 50A' in line:
			break
	csvfile.close()
	csvfile = itertools.islice(open('aa.csv'), n-1, None)

	#this method below uses dictreader to contain the column into array

	reader_dict = csv.DictReader(csvfile)
	number = 100
	for row in reader_dict:
		print(row['Time'], row['ISense 12V 50A'])
	#now the value can be compared with certain number
	#TODO: use compare_num method to compare with the
	#boudnary condition, make sure the comparaison ignores
	#the units and empty spots
		if int(row['Time']) == number:
			print "stop"
			break
