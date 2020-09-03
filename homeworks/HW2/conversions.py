# CSCI 1133, Lab Section 007, HW 1, Problem B
# Namita Nair, nair0025

def convert_pounds_to_kg(weight):
    weight = float(weight) * 0.454
    return weight

def convert_inches_to_cm(height):
    height = float(height) * 2.54
    return height

def h_and_b(weight, height, age, gender):
    convert_pounds_to_kg(weight)
    convert_inches_to_cm(height)
    if gender == 'f':
        bmr = 655.1 + (9.563 * float(weight)) + (1.850 * float(height)) - (4.676 * float(age))
        return bmr
    else:
        bmr = 66.5 + (13.75 * float(weight)) + (5.003 * float(height)) - (6.755 * float(age))
        return bmr
    
def r_and_s(weight, height, age, gender):
    convert_pounds_to_kg(weight)
    convert_inches_to_cm(height)
    if gender == 'f':
        bmr = 447.593 + (9.247 * float(weight)) + (3.098 * float(height)) - (4.330 * float(age))
        return bmr
    else:
        bmr = 88.362 + (13.397 * float(weight)) + (4.799 * float(height)) - (5.677 * float(age))
        return bmr
    
def m_and_s(weight, height, age, gender):
    convert_pounds_to_kg(weight)
    convert_inches_to_cm(height)
    if gender == 'f':
        bmr = (10.0 * float(weight)) + (6.25 * float(height)) - (5 * float(age)) - 161.0
        return bmr
    else:
        bmr = (10.0 * float(weight)) + (6.25 * float(height)) - (5 * float(age)) + 5.0
        return bmr

def main():
    weight = round(float(input("Weight in pounds:  ")), 2)
    height = round(float(input("Height in inches:  ")), 2)
    age = (int(input("Age:  ")))
    gender = input("Gender (m or f):  ")
    print("Your weight in kilograms:  ", round(convert_pounds_to_kg(weight), 2))
    print("Your height in centimeters:  ", round(convert_inches_to_cm(height), 2))
    print("Harris and Benedict BMR:  ", round(h_and_b(weight, height, age, gender), 2))
    print("Roza and Shizgal BMR:  ", round(r_and_s(weight, height, age, gender), 2))
    print("Mifflin and St Jeor BMR:  ", round(m_and_s(weight, height, age, gender), 2))
    
main()
