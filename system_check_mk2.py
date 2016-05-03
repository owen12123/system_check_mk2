#the goal of this program is to open csv file and analyze all the 
#values to the min and max values which are different in every 
#variable and if there's any value that is out of boundary, report
#which value is out of bound if not give a green sign to car

import csv
import itertools

#data compare method

def compare_num(a, max, min):
	if a>max:
		print "false"
		return false
	elif a<min:
		print "false"
		return false
	else:
		print "true"
		return true

# Binary select on 'expr' between 'true_' and 'false_' and return the result
def binary_select1(expr, true_, false_):
    if expr:
        return true_

    return false_
#question: is it better if we make a separate class and
#store all the data in that class? or make a hashtable?
#or build a csv file and import these data from it and compare 

with open('aa.csv') as csvfile_test:
	n = 0
	for line in csvfile_test.readlines():
		n += 1
		if 'ISense 12V 50A' in line:
			break
	csvfile_test.close()
	csvfile_test = itertools.islice(open('aa.csv'), n-1, None)

with open('system_max_min.csv') as csvfile_test_expect:
	#this method below uses dictreader to contain the column into array

    for row in csvfile_test_expect:
   		i=1
        irow = []
        for e_ in row:
			irow.append(binary_select1('m' in e_, e_, e_.replace(' ', '')))
			print irow[i]
			i+=1

	expect_range = csv.DictReader(csvfile_test_expect)
	test_values = csv.DictReader(csvfile_test)
	number = 100

	#get the names of all the sensors
#	for key, value in expect_range.items():
#		print key
#		print value

#	for row in expect_range:
#		print(row['Time'])
#		for row in test_values:
#			print(row['Time'])
			#compare_num(int(row['Time']), number, int(column['Time'])
#			print(lens(row['Time']), lens(row['ISense 12V 50A'])
		#now the value can be compared with certain number
		#TODO: use compare_num method to compare with the
		#boudnary condition, make sure the comparaison ignores
		#the units and empty spots
#			if int(row['Time']) == number:
#				print "stop"
#				break