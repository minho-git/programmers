# N(학생 수), M(비교 횟수)
# A B -> 학생 A가 학생 B 앞에 서야 한다.
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
lst = [[] for i in range(N+1)] # 인접 리스트
degree = [0] * (N+1) # 진입 차수 리스트

# 인접 리스트, 진입 차수 표현
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    lst[A].append(B)
    degree[B] += 1


que = deque()

for i in range(1, N+1):
    if degree[i] == 0:
        que.append(i)

while que:
    now = que.popleft()
    print(now, end=" ")

    for next in lst[now]:
        degree[next] -=  1
        if degree[next] == 0:
            que.append(next)

