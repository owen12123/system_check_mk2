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

# put the name, max and min of expected csv file into two dimensional array
def value(name):
    with open(name) as expect_csvfile:
        irow = []
        for line in expect_csvfile:
            irow.append(line.strip().split(','))
        return irow

def cutline(name):
    with open(name) as csvfile_test:
        n = 0
        for line in csvfile_test.readlines():
            n += 1
            if 'ISense 12V 50A' in line:
                # h = line.split(',')
                return n
                break
        csvfile_test.close()

def verify(test: str, veri: str):
        n = cutline(test)
        csvfile_test = itertools.islice(open(test), n - 1, None)

        # this method below uses dictreader to contain the column into array
        test_array = value(veri)
        reader_dict = csv.DictReader(csvfile_test)
        next(reader_dict)

        cols = len(value(veri)[0])
        for i in range(1, cols):
            #csvfile_test.seek(0)
            rows = list(reader_dict)
            for row in rows:
                if is_in_range(float(row[test_array[0][i]]), float(test_array[2][i]), float(test_array[1][i])) != True:
                    print('Fail :P')
                else:
                    print('True :D')
                    #make sure it goes to next column whenever it finishes it or finds an error value
            #make sure the next row will be analyzed

verify('aa.csv', 'system_max_min.csv')
