a = int(input("Enter a: "))

b = 1
count = 0

while count < a:
    print(b, end="")
    if count < a - 1:
        print(", ", end="")
    b += 2
    count += 1
