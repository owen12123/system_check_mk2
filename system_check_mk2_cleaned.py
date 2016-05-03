# the goal of this program is to open csv file and analyze all the
# values to the min and max values which are different in every
# variable and if there's any value that is out of boundary, report
# which value is out of bound if not give a green sign to car

import csv
import itertools


def is_in_range(value, min_, max_) -> bool:
    if min_ <= value <= max_:
        return True
    return False
# Binary select on 'expr' between 'true_' and 'false_' and return the result
# SEEMS WE WON'T NEED IT
def binary_select1(expr, true_, false_):
    if expr:
        return true_

    return false_

# put the name, max and min of expected csv file into two dimensional array
def value(name):
    with open(name) as expect_csvfile:
        irow = []
        for line in expect_csvfile:
            irow.append(line.strip().split(','))
        print(irow[0][0])
        return irow

def verify(test: str, veri: str):

    with open(test) as csvfile_test:
        n = 0
        for line in csvfile_test.readlines():
            n += 1
            if 'ISense 12V 50A' in line:
                # h = line.split(',')
                break
        csvfile_test.close()
        csvfile_test = itertools.islice(open('aa.csv'), n - 1, None)

        # this method below uses dictreader to contain the column into array

        reader_dict = csv.DictReader(csvfile_test)
        number = 100
        cols = len(value(veri)[0])
        for i in range(1, cols):
            for row in reader_dict:
                for row in reader_dict:
                    print(row[value(veri)[0][i]], int(value(veri)[1][i]), value(veri)[2][i])

verify('aa.csv', 'system_max_min.csv')
