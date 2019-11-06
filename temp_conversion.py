# Good practice to define your constants separately
us = "USA"
ger = "Germany"

# These are functions that can be used anywhere, so I took them out
def convert_f(fahrenheit):
    f = float(fahrenheit)
    f = (f * 9 / 5) + 32
    return f


def convert_c(celsius):
    c = float(celsius)
    c = (c - 32) * 5 / 9
    return c


# This is a main function, standard practice
def main():
    location = input("Are you from USA or Germany?\n")

    while True:
        if location in [ger, us]:
            print(f"You are from {location}.\n")
            break
        else:
            print("Enter the country Germany or USA.\n")

    # User input here
    # if else statements here

    recentLoc = input("What is your location right now?\n")

    temp = float(input("What is the temperature outdoor tomorrow?\n"))

    if recentLoc == ger and location == us:
        print(
            "Temperature for tomorrow is "
            + str(convert_c(temp))
            + " Celsius or "
            + str(convert_f(temp))
            + " Fahrenheit"
        )
    elif recentLoc == us and location == ger:
        print(
            "Temperature for tomorrow is "
            + str(convert_f(temp))
            + "Fahrenheit or "
            + str(convert_c(temp))
            + "Celsius"
        )
    elif recentLoc == us and location == us:
        print("Temperature for tomorrow is " + str(convert_f(temp)) + "Fahrenheit")
    elif recentLoc == ger and location == ger:
        print("Temperature for tomorrow is " + str(convert_c(temp)) + "Celsius")
    else:
        print("Please type in a number")


if __name__ == "__main__":
    main()
