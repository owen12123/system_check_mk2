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
def binary_select1(expr, true_, false_):
    if expr:
        return true_

    return false_

def verify(name: str, name1: str):
    with open(name1) as expect_csvfile:
        #for row in expect_csvfile:
        i=0
        irow = list(expect_csvfile)
#            for e_ in row: 
#                irow.append(binary_select1('m' in e_, e_, e_.replace(' ', '')))
#                print irow()
#                i+=1
        print(irow[i])

    with open(name) as csvfile_test:
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
        #for row in reader_dict:
            #print(row['Time'], row['ISense 12V 50A'])
            # break
            # question: can we compare the value of each row while it is sorting
            # in this for loop?
#            if int(row['Time']) >= number:
#               print("stop")
#                break


verify('aa.csv', 'system_max_min.csv')
