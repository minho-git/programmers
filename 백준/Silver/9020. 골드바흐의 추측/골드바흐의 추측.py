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
    j = 0
    min_gap = 10001
    min_num1 = 0
    min_num2 = 0

    while True:

        if primary_array[j] > num / 2:
            break


        if array[num - primary_array[j]] == 0: # 전체에서 소수를 뺀게 소수라면

            if min_gap > (num -primary_array[j]) - primary_array[j]: #
                min_num1 = primary_array[j]
                min_num2 = num - primary_array[j]
                min_gap = min_num2 - min_num1


        j += 1

    print(min_num1, min_num2)


