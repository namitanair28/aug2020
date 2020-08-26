# stretch 1, lab 4
# Namita Nair, nair0025

import random

def estimatePi(sampleSize):
    for i in range (0, sampleSize):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        r = (x ** 2 + y ** 2) ** .5
        count = 0
        if -1 <= r <= 1:
            count += 1
        else:
            count = count
    piEst = (count / sampleSize) * 4
    print(piEst)
    response = input("Do you wish to continue (y/n)? ")
    if response == 'y':
        main()
    else:
        return piEst
  
def main():
    sampleSize = int(input("Enter sample size to estimate pi: "))
    estimatePi(sampleSize)
    
main()