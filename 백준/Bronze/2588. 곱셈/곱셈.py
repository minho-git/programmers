num1 = int(input())
num2 = int(input())
result = num1 * num2

while True:
    if num2 < 1:
        break

    tmp = num1 * (num2 % 10)
    print(tmp)
    num2 =  int(num2 / 10)


print(result)
