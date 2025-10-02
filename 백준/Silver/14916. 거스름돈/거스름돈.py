n = int(input())

coins = [5, 2]
answer = 0

tmp = n // 2
flag = True

for i in range(0, tmp + 1):
    if (n - (2 * i)) % 5 == 0:
        answer += (n - (2 * i)) // 5
        break
    else:
        answer += 1
else:
    flag = False
    print(-1)



if flag:
    print(answer)

