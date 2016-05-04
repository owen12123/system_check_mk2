# the goal of this program is to open csv file and analyze all the
# values to the min and max values which are different in every
# variable and if there's any value that is out of boundary, report
# which value is out of bound if not give a green sign to car

import csv
import itertools
import cProfile


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
                return n
        csvfile_test.close()


def compare(test, array, number):
    for row in array:
        if not is_in_range(float(row[test[0][number]]),
                            float(test[2][number]),
                            float(test[1][number])):
            return False
        else:
            return True


def verify(test: str, veri: str):
    n = cutline(test)
    csvfile_test = itertools.islice(open(test), n - 1, None)

    # this method below uses dictreader to contain the column into array
    test_array = value(veri)
    reader_dict = csv.DictReader(csvfile_test)
    next(reader_dict)
    cols = len(test_array[0])

    for i in range(1, cols):
        if compare(test_array, reader_dict, i):
            print(test_array[0][i]+'\t\t is good')
        else:
            print(test_array[0][i]+'\t\t failed')


verify('aa.csv', 'system_max_min.csv')
#cProfile.run("verify('aa.csv', 'system_max_min.csv')")

