# Namita Nair, hw2c

def forecast():
    print("Answer each question with a 'yes' or a 'no'.")
    first = input("Is the temperature higher than 70 degrees farenheit? ")
    if first == 'yes':
        second = input("Is the wind faster than 2 mph? ")
        if second == 'yes':
            third = input("Is the air pressure greater than 26 inHg? ")
            if third == 'yes':
                return "rain"
            else:
                return "no rain"
        else:
            return "no rain"
    else:
        fourth = input("Is the wind faster than 4.5 mph? ")
        if fourth == 'yes':
            return "rain"
        else:
            fifth = input("Is the air pressure greater than 31 inHG? ")
            if fifth == 'yes':
                return "rain"
            else:
                return "no rain"
                        
def main():
    forecast()
main()
