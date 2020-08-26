#Lab 12, section 007
#Namita Nair, nair0025
#import turtle
##myt = turtle.Turtle()
#
#scr = turtle.Screen()
#scr.delay(0)
#myt.speed(0)
#myt.hideturtle()
#
#def mouseInput(x,y):
#    print(x, ' , ' ,y)
#    
#scr.online(mouseInput)
#scr.listen()

#stretch 1
import random
import turtle
myt = turtle.Turtle()

def randColor():
    color = random.choice(["red", "yellow", "green", "blue", "purple", "orange"])
    return color

print(randColor())
#2
class Shape:

    def __init__(self, fillcolor = "", location = (0,0), filled = False):
        self.fillcolor = fillcolor
        self.location = location
        self.filled = filled
        
    def setFillcolor(self, str):
        self.fillcolor = str
        
    def setFilled(self, bool):
        self.filled = bool
        
    def isFilled(self):
        return self.filled
    
#3
class Circle(Shape):
    
    def __init__(self, x = 0, y = 0, r = 1):
        self.x = x
        self.y = y
        self.r = r
        
    def draw(self, turtle):
        myt.penup()
        myt.goto(self.x, self.y)
        myt.circle(self.r)
        if self.filled == True:
            myt.fillcolor(self.fillcolor)
            myt.behin_fill()
            myt.circle(self.r)
            myt.end_fill()
    
#workout
class Display:
    
    def __init__(self, myt=turtle.Turtle(), scr=turtle.Screen()):
        self.myt = myt
        self.scr = scr
        
    def mouseEvent(self, x, y)
            
            
            
            
            
        