A = int(input())
B = int(input())
C = int(input())

mul = A * B * C
count = [0] * 10

while True:
    if mul < 1:
        break


    count[mul % 10] += 1
    mul = int(mul/10)

for i in count:
    print(i)
