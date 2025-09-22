import sys

sys.setrecursionlimit(10 ** 6)

# N(노드 개수), M(질의 개수),
# 0 a b -> union
# 1 a b -> find

N, M = map(int, sys.stdin.readline().split())

# 처음에는 노드가 연결돼 있지 않으므로 각 노드의 대표 노드는 자기 자신이다. 각 노드를 자신의 인덱스 값으로 초기화 한다
parent = [i for i in range(N+1)]

def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a]) # 재귀 형태로 표현 -> 경로 압축
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def check_same(a, b):
    a = find(a)
    b = find(b)

    return a == b

for i in range(M):
    question, a, b = map(int, sys.stdin.readline().split())
    if question == 0:
        union(a, b)
    else:
        if check_same(a, b):
            print("YES")
        else:
            print("NO")




