loan_amount = float(input("Enter loan amount: "))
r = float(input("Enter annual interest rate: "))
n = float(input("Enter loan duration in months: "))
payment = (r*loan_amount)/(1-(1+r)**(-n))
print("Monthly payment: ", payment)

