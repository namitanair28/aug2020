# Warm-up: Rounding floating-point values
# Namita Nair, nair0025

def roundFloat(x):
    if x > 0:
        xi = int(x + 0.5)
        return(xi)
    elif x < 0:
        xi = int(x - 0.5)
        return(xi)
    else:
        return("Error: Enter floating-point value: ")
        main()

def main():
    x = float(input("Enter a floating-point value: "))
    print(roundFloat(x))

main()
