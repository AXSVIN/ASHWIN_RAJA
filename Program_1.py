a = float(input("Enter a: "))
b = float(input("Enter b: "))

print("Select operation type:")
print("1 - Add")
print("2 - Sub")
print("3 - Mul")
print("4 - Div")

optn = int(input("Enter operation number (1/2/3/4): "))

if optn == 1:
    result = a + b
    print(result)
elif optn == 2:
    result = a - b
    print(result)
elif optn == 3:
    result = a * b
    print(result)
elif optn == 4:
    if b != 0:
        result = a / b
        print(result)
    else:
        print("Error")
else:
    print("Invalid operation type.")
