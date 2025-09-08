import sys


def travel_city(cost, count, visited, start, origin):
    global min_cost, N
    if count == N:
        if board[start][origin] != 0:
            cost += board[start][origin]
            min_cost = min(min_cost, cost)
            return

    if cost > min_cost:
        return

    for i in range(N):
        if not visited[i] and board[start][i] != 0:
            visited[i] = True

            travel_city(cost + board[start][i], count+1, visited, i, origin)

            visited[i] = False

N = int(input())

origin = 0
board = []
min_cost = sys.maxsize

for i in range(N):
    board.append(list(map(int, input().split())))


for i in range(N):
    origin = i
    visited_city = [False for j in range(N)]
    visited_city[i] = True
    count = 1
    cost = 0

    travel_city(cost, count, visited_city, i, origin)
    visited_city[i] = False

print(min_cost)



