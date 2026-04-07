N, C = map(int, input().split())
graph = []
answer = 1

for i in range(N):
    graph.append(int(input()))

graph.sort()

start = 1
end = graph[-1] - graph[0]

while start <= end:
    mid = (start + end) // 2
    count = 1
    tmp = mid

    for i in range(1, N):
        tmp -= (graph[i] - graph[i-1])

        if tmp <= 0:
            count += 1
            tmp = mid

    if count >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
