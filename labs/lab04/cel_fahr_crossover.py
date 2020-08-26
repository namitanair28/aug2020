# lab 4, warm-up 1
# Namita Nair, nair0025

def celsFahr():
    celsius = 100
    fahrenheit = int((9 / 5) * celsius + 32)
    while celsius != fahrenheit:
        celsius -= 1
        fahrenheit = int((9 / 5) * celsius + 32)
    print (celsius, fahrenheit)

celsFahr()