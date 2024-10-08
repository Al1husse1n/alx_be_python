def safe_divide(numerator, denominator):
    try :
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    try :
        return f'The result of the division is {num / denom}'
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
