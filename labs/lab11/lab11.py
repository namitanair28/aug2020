#Lab 11 Section 007
#Namita Nair, nair0025

#Problem 1

class measure:
    
    def __init__(self, feet=0, inches=0):
        self.feet = feet
        self.inches = inches
        
    def __str__(self):
        return (str(self.feet) + '\'' + str(self.inches) + '\"')
    
    def __add__(self, other):
        feet = self.feet + other.feet
        inches = self.inches + other.inches
        return measure(feet, inches)
    
    def __sub__(self, other):
        feet = self.feet - other.feet
        inches = self.inches - other.inches
        return measure(feet, inches)
    
m1 = measure()
m2 = measure(4, 11)
m3 = measure(6, 10)
#print(m1)
#print(m1 + m3)
#print(m3 - m2)

#Problem 2

class vector:
    
    def __init__(self, vector = [0,0,0]):
        self.vector = vector
        
    def __str__(self):
        return (str(self.vector))
    
    def getValues(self):
        newlist = []
        for i in self.vector:
            newlist.append(i)
        return newlist
    
    def setValues(self, list1):
        self.vector = self.vector.extend(list1)
        return self.vector
    
    def magnitude(self):
        sum1 = 0
        for i in self.vector:
            sum1 += i**2
        magnitude = sum1**0.5
        return magnitude
    
    def __add__(self, other):
        
    def __mul__(self, other):
            
    
    
    
v1 = vector([1,2,3])
print(v1)
    
        




















