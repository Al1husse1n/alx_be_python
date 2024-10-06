def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        print(f'The result of the division is {num / denom}')
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")  