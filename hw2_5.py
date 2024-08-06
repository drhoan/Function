# Write a function called km_to_miles that takes kilometers as a parameter,
# converts it into miles and returns the result.
# For example, km_to_miles(1) should return 0.621371.
def km_to_miles(km):
    return km / 1.60934

if __name__ == "__main__":
    km = float(input("Enter a distance in kilometers: "))
    print(f'{km} kilometers is {km_to_miles(km):.1f} miles')

