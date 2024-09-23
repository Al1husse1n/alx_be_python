def perform_operation(num1,num2,operation):
    match operation:
        case "add":
            print(num1 + num2)
        case "subtract":
            print(num2 + num1)
        case "multiply":
            print(num1 * num2)
        case "divide":
            if num1 == 0:
                print("You can't divide a number by zero")
            else:
                print(num2 / num1)



