FAHRENHEIT_TO_CELSIUS_FACTOR = (5 / 9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9 / 5)

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
def main():
    try:
        temp_to_convert = float(input("Enter the temperature to convert: "))
        temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")   
        match temp_type:
            case 'C':
                fahr = convert_to_fahrenheit(temp_to_convert)
                print(f'{temp_to_convert}ºc is {fahr}ºf')
            case 'F':
                cels = convert_to_celsius(temp_to_convert)  
                print(f'{temp_to_convert}ºf is {cels}ºc')
            case _:
                print("invalid Temperature type")
    except ValueError :
        print("Invalid temperature. Please enter a numeric value.")                
if __name__ == "__main__":
    main()                      