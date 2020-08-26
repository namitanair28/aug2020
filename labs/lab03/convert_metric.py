# stretch: metric conversions
# Namita Nair, nair0025

def convert(x,y):
    if y == 'pounds':
        z = "{0:.4f}".format(x * 0.454)
        print(z, 'kilos')
    elif y == 'ounces':
        z = "{0:.4f}".format(x * 28.35)
        print(z, 'grams')
    elif y == 'miles':
        z = "{0:.4f}".format(x * 1.609)
        print(z, 'kilometers')
    elif y == 'inches':
        z = "{0:.4f}".format(x * 2.54)
        print(z, 'centimeters')
    elif y == 'kilos':
        z = "{0:.4f}".format(x * 2.205)
        print(z, 'pounds')
    elif y == 'grams':
        z = "{0:.4f}".format(x * 0.0353)
        print(z, 'ounces')
    elif y == 'kilometers':
        z = "{0:.4f}".format(x * 0.621)
        print(z, 'miles')
    elif y == 'centimeters':
        z = "{0:.4f}".format(x * 0.394)
        print(z, 'inches')
    else:
        print("Error: invalid units")

def main():
    x = float(input("Enter value: "))
    y = input("Enter units: ")
    convert(x,y)
    check = input("Do you wish to continue (y/n)?")
    if check == y:
        main()
    else:
        print("Finished.")
    
main()
