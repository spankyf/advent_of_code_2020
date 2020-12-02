import pandas as pd

data = pd.read_csv('01.csv', header=None)

target = 2020


def two_integers(data):
    for datapoint in data[0].values:
        remainder = target - datapoint
        if remainder in data[0].values:
            print(target, datapoint, remainder)
            print(datapoint * remainder)
            return


def three_integers(data):

    for datapoint in data[0].values:
        vals_popped_one = data[0].values.tolist()
        vals_popped_one.remove(datapoint)
        for remaining_val in vals_popped_one:
            remainder = target - datapoint - remaining_val
            if remainder > -1 and remainder in data[0].values:
                print(datapoint * remaining_val * remainder)
                return
