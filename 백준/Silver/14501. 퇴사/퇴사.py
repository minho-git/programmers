N = int(input())
graph = [(0, 0)]
dp = [0] * (N+2)


for i in range(N):
    graph.append(tuple(map(int, input().split())))


for i in range(1, N+1):
    clear_day = i + graph[i][0]

    if clear_day <= N+1:
        for j in range(clear_day, N+2):
            dp[j] = max(dp[j], dp[i] + graph[i][1])

print(max(dp))