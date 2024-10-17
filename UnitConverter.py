def length_converter():
    print("\nLength Converter:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        km = float(input("Enter value in kilometers: "))
        miles = km * 0.621371
        print(f"{km} km is equal to {miles:.2f} miles.")
    elif choice == '2':
        miles = float(input("Enter value in miles: "))
        km = miles / 0.621371
        print(f"{miles} miles is equal to {km:.2f} km.")
    else:
        print("Invalid choice!")

def temperature_converter():
    print("\nTemperature Converter:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")
    else:
        print("Invalid choice!")

def main():
    print("Welcome to the Unit Converter!")
    print("1. Length Converter")
    print("2. Temperature Converter")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        length_converter()
    elif choice == '2':
        temperature_converter()
    else:
        print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
