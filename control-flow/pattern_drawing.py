inp = int(input("Enter the size of the pattern: "))
x = 0
for i in range(inp):
    while x < 4:
        print("*", end="")
        x += 1
    x = 0    
    print()    