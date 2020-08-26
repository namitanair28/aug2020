# Lab Section 007, lab 05 warm up
# nair0025, Namita Nair

import random

def histograms():
    count12 = 0
    count11 = 0
    count10 = 0
    count9 = 0
    count8 = 0
    count7 = 0
    count6 = 0
    count5 = 0
    count4 = 0
    count3 = 0
    count2 = 0
    for i in range (10000):
        first = random.randint(1,6)
        second = random.randint(1,6)
        sum = first + second
        if sum == 12:
            count12 += 1
        if sum == 11:
            count11 += 1
        if sum == 10:
            count10 += 1
        if sum == 9:
            count9 += 1
        if sum == 8:
            count8 += 1
        if sum == 7:
            count7 += 1
        if sum == 6:
            count6 += 1
        if sum == 5:
            count5 += 1
        if sum == 4:
            count4 += 1
        if sum == 3:
            count3 += 1
        if sum == 2:
            count2 += 1
    print('2:', format(count2, "5d"))
    print('3:', format(count3, "5d"))
    print('4:', format(count4, "5d"))
    print('5:', format(count5, "5d"))
    print('6:', format(count6, "5d"))
    print('7:', format(count7, "5d"))
    print('8:', format(count8, "5d"))
    print('9:', format(count9, "5d"))
    print('10:', format(count10, "5d"))
    print('11:', format(count11, "5d"))
    print('12:', format(count12, "5d"))
histograms()