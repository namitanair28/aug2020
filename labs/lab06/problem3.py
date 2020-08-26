# Lab 06, Problem 3
# nair0025, Namita Nair, lab section 007

def DetermineCholesterolRatio(total, hdl):
    ratio = float(total/hdl)
    if ratio <= 3.5:
        return str(ratio) + ": less than average risk"
    elif ratio > 3.5 and ratio <= 4.5:
        return str(ratio) + ": average risk"
    else:
        return str(ratio) + ": high risk"
    
def main():
    print(DetermineCholesterolRatio(200, 40))
main()