N = int(input())
arr = [[0, 0, 0]]
dy = [0]

for i in range(N):
    arr.append(list(map(int, input().split())))
    arr[i+1].append(i+1)

arr.sort(key=lambda x : x[0])

dy = [[1, 0]]

for i in range(1, N+1):
    dy.append([arr[i][1],0]) # 여기가 문제! 자기 밑에 벽돌의 인덱스를 넣어야하는데 자기 자신을 넣고 있었음.

for i in range(2, N+1):
    for j in range(i-1, 0, -1):

        if arr[i][2] > arr[j][2]:
            if dy[i][0] < dy[j][0] + arr[i][1]:
                dy[i][0] = dy[j][0] + arr[i][1]
                dy[i][1] = j

_max = 0
_max_index = 0
for index, value in enumerate(dy):
    if _max < value[0]:
        _max = value[0]
        _max_index = index

reverse_arr = [_max_index]
while True:
    if dy[_max_index][1] == 0:
        break

    reverse_arr.append(dy[_max_index][1])
    _max_index = dy[_max_index][1]

reverse_arr.reverse()
print(len(reverse_arr))
for i in reverse_arr:
    print(arr[i][3])


