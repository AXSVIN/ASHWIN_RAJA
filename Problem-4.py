input_list = list(map(int, input("Enter numbers separated by space: ").split()))

result = {}

for i in range(1, 10):
    count = 0
    for num in input_list:
        if num % i == 0:
            count += 1
    result[i] = count

print(result)
