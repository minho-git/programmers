N = int(input())
total = 0

number = int(input())

for i in range(1, N+1):
    total += number % 10
    number //= 10

print(total)

