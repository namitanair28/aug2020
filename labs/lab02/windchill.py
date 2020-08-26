t = int(input("Enter temperature in degrees Farenheit: "))
v = int(input("Enter wind velocity in miles/hour: "))
windChill = 35.74+(0.6215*t)-(35.75*(v**0.16))+(0.4275*t*(v**0.16))
print("Wind Chill: ", windChill)
