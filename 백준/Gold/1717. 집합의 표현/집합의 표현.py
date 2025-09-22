import sys

# Python의 기본 재귀 깊이 제한은 1,000이므로, 
# 노드의 개수가 많을 경우를 대비해 재귀 깊이를 10^6까지 늘림
sys.setrecursionlimit(10 ** 6)

# N: 노드의 개수, M: 질의(연산)의 개수
# sys.stdin.readline()을 사용하여 입력을 빠르게 처리
N, M = map(int, sys.stdin.readline().split())

# 각 노드의 부모 노드를 저장하는 리스트
# 처음에는 모든 노드가 자기 자신을 부모로 가리키도록 초기화
# 예: parent[3] = 3
parent = [i for i in range(N + 1)]


# --- 함수 정의 ---

# 특정 노드 a의 대표 노드(루트)를 찾는 함수
def find(a):
    # 1. 기저 조건(Base Case): 만약 노드 a의 부모가 자기 자신이면, a는 루트 노드임
    if parent[a] == a:
        return a

    # 2. 경로 압축(Path Compression): 재귀적으로 루트를 찾아 올라가면서
    #    경로상의 모든 노드들의 부모를 최종 루트로 직접 연결함
    #    이를 통해 트리의 높이를 낮춰 시간 복잡도를 최적화
    parent[a] = find(parent[a])
    return parent[a]


# 두 노드 a와 b가 속한 집합을 합치는 함수
def union(a, b):
    # find 함수를 호출하여 각 노드의 대표 노드를 찾음
    root_a = find(a)
    root_b = find(b)

    # 두 노드의 대표 노드가 다르다면, 아직 다른 집합에 속해 있다는 의미
    if root_a != root_b:
        # 한쪽의 대표 노드를 다른 쪽의 대표 노드의 자식으로 만들어 두 집합을 합침
        # 여기서는 b의 대표 노드가 a의 대표 노드를 가리키도록 설정
        parent[root_b] = root_a


# 두 노드 a와 b가 같은 집합에 속해 있는지 확인하는 함수
def check_same_set(a, b):
    # 각 노드의 대표 노드를 찾음
    root_a = find(a)
    root_b = find(b)

    # 두 노드의 대표 노드가 같다면, 같은 집합에 속해 있다는 의미
    if root_a == root_b:
        print("YES")
    else:
        print("NO")


# --- 메인 로직 ---
# M개의 질의(연산)를 처리하기 위해 반복
for _ in range(M):
    # 연산의 종류(question)와 두 노드(a, b)를 입력받음
    question, a, b = map(int, sys.stdin.readline().split())

    # question이 0이면 union 연산을 수행
    if question == 0:
        union(a, b)
    # question이 1이면 두 노드가 같은 집합인지 확인하는 연산을 수행
    else:
        check_same_set(a, b)