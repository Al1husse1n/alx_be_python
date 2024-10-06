def safe_divide(numerator, denominator):
    try :
        num = float(numerator)
        denom =float(denominator)
    except ValueError:
        print("Error: Please enter numeric values only.")
    try :
        print(f'The result of the division is {numerator / denominator}')
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.") 
        