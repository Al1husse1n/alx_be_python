FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp_to_convert = input("Enter the temperature to convert: ")
temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if not temp_to_convert.replace('.', '', 1).isdigit():
    print("Invalid temperature. Please enter a numeric value.")
else:    
    match temp_type:
        case 'C':
            fahr = convert_to_fahrenheit(float(temp_to_convert))
            print(f'{float(temp_to_convert)}ºc is {fahr}ºf')
        case 'F':
            cels = convert_to_celsius(float(temp_to_convert))  
            print(f'float({temp_to_convert})ºf is {cels}ºc')
        case _:
            print("invalid Temperature type")       