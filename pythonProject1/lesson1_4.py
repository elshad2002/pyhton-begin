num = int(input("Enter your number:"))
print(num)
max = 0
while num != 0:
    if num % 10 > max:
        max = num % 10
    num = num // 10
print(max)
