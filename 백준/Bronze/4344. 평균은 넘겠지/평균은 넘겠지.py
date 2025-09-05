C = int(input())

for i in range(C):

    array = list(map(int, input().split()))
    people = array[0]

    sum = 0
    for j in range(1, people + 1):
        sum += array[j]

    avg = sum / people

    count = 0
    for j in range(1, people + 1):
        if array[j] > avg:
            count += 1

    print(f"{round(count / people * 100, 3)}%")






