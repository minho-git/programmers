N = int(input())

for i in range(N):
    array = list(input())
    score = 0
    sum = 0
    for j in range(len(array)):
        if array[j] == 'O':
            score += 1
            sum += score
        else:
            score = 0

    print(sum)

