location = input("Are you from USA? or Germany?")

us = ("USA")
ger = ("Germany")

if location == ger:
    print("You are from Germany")
elif location == us:
    print("You are from the USA")
else:
    print("Enter the country Germany or USA")

# User input here
# if else statements here

recentLoc = input("What is your location right now?")

temp = float(input("What is the temperature outdoor tomorrow?"))

def convert_f(fahrenheit):
    f = float(fahrenheit)
    f = (f*9/5)+32
    return(f)

def convert_c(celsius):
    c = float(celsius)
    c = (c-32)*5/9
    return(c)

if recentLoc == ger and location == us:
    print("Temperature for tomorrow is " + convert_c(temp) + "Celsius or " + convert_f(temp) + "Fahrenheit")
elif recentLoc == us and location == ger:
    print("Temperature for tomorrow is " + convert_f(temp) + "Fahrenheit or " + convert_c(temp) + "Celsius")
elif recentLoc == us and location == us:
    print("Temperature for tomorrow is " + convert_f(temp) + "Fahrenheit")
elif recentLoc == ger and location == ger:
    print("Temperature for tomorrow is " + convert_c(temp) + "Celsius")
else:
    print("Please type in a number")