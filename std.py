import math
import sys


def main():

    while True:
        # input data as numbers
        try:
            data = input("enter digits and spaces between them: ").strip().split(' ')
            data = list(data)
            # convert elements into float
            intdata = [float(i) for i in data]
            std(intdata)
            break

        except ValueError:
            print("usage: enter numbers only and one spaces in between")


def std(datapoints):
    # first lets caluclate the mean
    mean = sum(datapoints)/len(datapoints)
    print(f"mean is: {mean}")
    # calculate each datapoint distance from mean
    distance = {}
    for i in datapoints:
        distance[i] = (i - mean) ** 2

    print(f"distances is {distance}")
      

    distancesum = sum(distance.values())
    variance = distancesum/len(datapoints)
    std = math.sqrt(variance)

    print("std is square root of sum distances from the mean and devide over number of datapoints: {%.2f} " % std)


if __name__ == '__main__':
    main()
