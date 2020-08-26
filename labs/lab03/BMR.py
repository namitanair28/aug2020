# Warm-up: Basal Metabolic Rate
# Namita Nair, nair0025

def BMR():
    weight = int(input("Enter weight in pounds: "))           
    height = int(input("Enter height in inches: "))
    age = int(input("Enter age in years: "))         
    gender = input("Enter M for male or F for female: ")
    if gender == 'F':
        value = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
        print(value)

    elif gender == 'M':
        value = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
        print(value)
        
    else:
        print("Error: enter M or F")
        BMR()

BMR()
