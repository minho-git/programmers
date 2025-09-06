start_array = []
end_array = []


def hanoi(start, end, count, other):

    if count == 1:
        start_array.append(start)
        end_array.append(end)
        return 1

    return hanoi(start, other, count-1, end) + hanoi(start, end, 1, other) + hanoi(other, end, count-1, start)

N = int(input())

if N <= 20:
    print(hanoi(1, 3, N, 2))
    for i in range(len(start_array)):
        print(start_array[i], end_array[i])
else:
    print(2 ** N - 1)
