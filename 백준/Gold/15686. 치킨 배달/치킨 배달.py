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

dfs(0, 0)
print(res)

