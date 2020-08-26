#Namita Nair, Lab Section 007
#Lab 7, Warm-up
import random


filename = input("Enter file name: ")+".csv"
fileobj = open(filename, 'w')
record = ''
for i in range(1000):
    record += str(i+1)+","+str(random.randint(-1000,1000))+"\n"    
fileobj.write(record)
fileobj.close()
