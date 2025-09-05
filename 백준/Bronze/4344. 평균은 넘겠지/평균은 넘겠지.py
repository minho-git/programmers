C = int(input())

for i in range(C):

    array = list(map(int, input().split()))
    people = array[0]

    avg = sum(array[1:])/array[0]

    count = 0
    for j in array[1:]:
        if j > avg:
            count += 1

    print(f"{round(count / people * 100, 3)}%")






