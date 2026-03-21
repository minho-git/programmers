# 9:45 시작
from collections import deque

# 0: 빈칸
# 1: 집
# 2: 피자집

# 번호는 1 ~ N

# 피자 배달 거리: 집과 피자집들과의 거리 중 최소값 = |x1 - x2| + |y1 - y2|
# 도시의 피자 배달 거리: 각 집들의 피자 배달 거리 합한 것
# M개의 피자집만 선택

# 피자 집을 어떻게 선택하지? -> 이걸 dfs로?
# M개 만큼만 2를 남겨둔 상태에서
# DFS를 돌아야한다.
# 그리고 1을 만나면 그 격자의 값보다 작으면 값을 바꾼다.
# 그러고 값이 무한대가 아닌것만 다 더해서 최솟값을 구해서 res 에 넣는다.
# 이걸 계속 최소값으로 바꾼다.

N, M = map(int, input().split())
graph = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
res = float("inf")

for i in range(N):
    graph.append(list(map(int, input().split())))

pizza = []
house = []
real_pizza = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            pizza.append((i, j))
        elif graph[i][j] == 1:
            house.append((i, j))


# def find_min_distance():
# #     global res
# #
# #     check = [[float("inf")] * N for _ in range(N)]
# #     tmp = 0
# #
# #     for i in range(N):
# #         for j in range(N):
# #             if graph[i][j] == 2:
# #                 visited = [[0] * N for _ in range(N)]
# #                 q = deque()
# #                 q.append((i, j, 0))
# #                 visited[i][j] = 1
# #
# #                 while q:
# #                     y, x, l = q.popleft()
# #
# #                     if graph[y][x] == 1:
# #                         check[y][x] = min(check[y][x], l)
# #
# #                     for k in range(4):
# #                         yy = y + dy[k]
# #                         xx = x + dx[k]
# #
# #                         if 0 <= yy < N and 0 <= xx < N and not visited[yy][xx]:
# #                             visited[yy][xx] = 1
# #                             q.append((yy, xx, l + 1))
# #
# #     for ii in range(N):
# #         for jj in range(N):
# #             if check[ii][jj] != float("inf"):
# #                 tmp += check[ii][jj]
# #
# #     res = min(res, tmp)

def find_min_distance():
    global res
    distance = [float("inf")] * len(house)

    for i in range(len(house)):
        y, x = house[i]

        for yy, xx in real_pizza:
            distance[i] = min(distance[i], abs(y - yy) + abs(x - xx))

    res = min(res, sum(distance))

def dfs(index, level):
    global res

    if level == M:
        find_min_distance()
        return

    if index == len(pizza):
        return

    # 피자집을 선택안했을때
    dfs(index + 1, level)

    # 피자집을 선택했을때
    real_pizza.append(pizza[index])
    dfs(index + 1, level + 1)
    real_pizza.pop()

# def dfs(index, level):
#     global res
#
#     if level == M:
#         find_min_distance()
#         return
#
#     if index == len(pizza):
#         return
#
#     # 피자집을 선택했을때
#     dfs(index + 1, level + 1)
#
#     # 피자집을 선택안했을때
#     graph[pizza[index][0]][pizza[index][1]] = 0
#     dfs(index + 1, level)
#     graph[pizza[index][0]][pizza[index][1]] = 2

dfs(0, 0)
print(res)















