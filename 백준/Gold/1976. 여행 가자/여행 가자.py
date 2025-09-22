# N(도시 수) <= 200
# M <= 1000
# 여행 경로가 가능한지 알아보자 -> 같은 집합인가? 연결되어있는가? -> 유니온 파인드를 이용하자

def find(a):
    if root_city[a] == a:
        return a

    root_city[a] = find(root_city[a])
    return root_city[a]

def union(a, b):
    a = find(a)
    b = find(b)

    # 같은 집합으로 만들기
    if a != b:
        root_city[b] = a


N = int(input())
M = int(input())
#    j
# i  0 1 0
#    1 0 1
#    0 1 0

# 도시의 연결을 기록할 그래프를 만들다. 연결 리스트로 만들자.
graph = [[]]
for i in range(N):
    tmp = [0]
    graph.append(tmp + list(map(int, input().split())))

# 부모 도시를 표현할 그래프로 만들자. 처음은 자기 자신 값을 가진다.
root_city = []
for i in range(N+1):
    root_city.append(i)

# 그래프를 돌면서 1인것들을 유니온 하자.
for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == 1:
            union(i, j)

# 방문 할 도시들이 다 같은지 확인하자.
visit_city = list(map(int, input().split()))


#union 연산은 두 집합의 대표 노드만 연결할 뿐,
# 합쳐진 집합 내 모든 노드의 부모 값을 즉시 통일시켜 주지는 않습니다.
# 따라서 두 노드가 같은 집합인지 확인할 때는 부모 리스트의 값을 직접 비교하면 안 되며,
# 반드시 find 함수를 통해 각 노드의 최종 대표 노드가 같은지 확인해야 합니다.
flag = True

root = find(visit_city[0])
for i in range(1, len(visit_city)):
    if root != find(visit_city[i]):
        flag = False


if flag:
    print("YES")
else:
    print("NO")


