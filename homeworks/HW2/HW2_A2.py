# CSCI 1133, Lab Section 007, HW 1, Problem A2
# Namita Nair, nair0025

def subtractFor(total, num, times):
    if times >= 0:
        answer = total - num * times
        return answer
    else:
        print("Error: number of times subtracted cannot be less than 0")
    
def main():
    total = int(input("Please enter the current total:  "))
    num = int(input("What number will be subtracted?  "))
    times = int(input("How many times should we subtract?  "))
    print("Answer:  ", total, " - ( ", num, " * ", times, " ) = ", subtractFor(total, num, times))
    
main()