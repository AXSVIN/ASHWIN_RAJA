a = int(input("Enter a: "))

b = 1
count = 0

limit = a
if a % 2 == 0:
    limit = a - 1  



while count < limit:
    print(b, end="")
    if count < limit - 1:
        print(", ", end="")
    b += 2
    count += 1


