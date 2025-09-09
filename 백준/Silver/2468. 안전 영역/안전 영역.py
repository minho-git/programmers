import sys

sys.setrecursionlimit(10**6)

def dfs(y, x, heights, visited, height):
    global N, dirY, dirX
    visited[y][x] = True

    for k in range(4):
        newY = y + dirY[k]
        newX = x + dirX[k]

        if 0 <= newY < N  and 0 <= newX < N and not visited[newY][newX] and heights[newY][newX] > height:
            dfs(newY, newX, heights, visited, height)




N = int(input())
answer = 0

dirY = [-1, 0, 1, 0]
dirX = [0, 1, 0, -1]
heights = []
max_height = 0

for i in range(N):
    heights.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        max_height = max(max_height, heights[i][j])

for k in range(0, max_height + 1):
    visited = [[False for i in range(N)] for j in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and heights[i][j] > k:
                dfs(i, j, heights, visited, k)
                count += 1

    answer = max(answer, count)

print(answer)






