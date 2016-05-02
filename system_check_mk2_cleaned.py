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


def verify(name: str):
    with open(name) as csvfile:
        n = 0
        for line in csvfile.readlines():
            n += 1
            if 'ISense 12V 50A' in line:
                # h = line.split(',')
                break
        csvfile.close()
        csvfile = itertools.islice(open('aa.csv'), n - 1, None)

        # this method below uses dictreader to contain the column into array

        reader_dict = csv.DictReader(csvfile)
        number = 100
        for row in reader_dict:
            print(row['Time'], row['ISense 12V 50A'])
            # break
            # question: can we compare the value of each row while it is sorting
            # in this for loop?
            if int(row['Time']) == number:
                print("stop")
                break


verify('aa.csv')
