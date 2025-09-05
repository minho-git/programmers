N = int(input())

for i in range(N):
    array = input()
    score = 0
    sumScore = 0

    for j in array:
        if j == 'O':
            score += 1
        else:
            score = 0

        sumScore += score

    print(sumScore)