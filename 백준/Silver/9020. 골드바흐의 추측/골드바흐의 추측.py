# 소수인 배열을 만들어 놓고
# 주어진 수에서 첫 번째 소수부터 빼서 그 수가 소수이면 출력!
array = [0 for i in range(10001)]
array[1] = 1
array[0] = 1

primary_array = []

for i in range(2, int(10000**0.5)+1):
    for j in range(i*i, 10000+1, i):
        array[j] = 1

for i in range(10001):
    if array[i] == 0:
        primary_array.append(i)

N = int(input())

for i in range(N):
    num = int(input())

    for j in range(num//2, 1, -1):
        if array[j] == 0 and array[num - j] == 0:
            print(j, num-j)
            break
