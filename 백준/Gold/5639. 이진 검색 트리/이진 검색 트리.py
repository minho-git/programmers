# '첫번째요소' 파라미터는 혼란을 주고 필요 없으므로 제거합니다.
def dfs(짜른배열, 딕셔너리):
    # 수정 1: 베이스 케이스를 맨 위로!
    # 처리할 배열이 비어있으면 할 일이 없으므로 즉시 종료시킵니다.
    if not 짜른배열:
        return

    # 수정 2: '루트'를 현재 배열의 첫 요소로 명확하게 정의합니다.
    root = 짜른배열[0]

    # 수정 3: 오른쪽 경계선(split_point) 찾기
    # 비교 대상을 '첫번째요소'가 아닌 현재 'root'로 변경합니다.
    split_point = len(짜른배열)
    for i in range(1, len(짜른배열)):
        if 짜른배열[i] > root:
            split_point = i
            break

    # 왼쪽과 오른쪽 서브트리 배열을 나눕니다.
    left_subarray = 짜른배열[1:split_point]
    right_subarray = 짜른배열[split_point:]

    # 수정 4: 노드 연결 로직을 완전히 새로 구성합니다.
    # 'root'를 기준으로 왼쪽/오른쪽 자식을 연결하고, 그 다음에 재귀 호출을 합니다.

    # 왼쪽 자식이 실제로 존재하면
    if left_subarray:
        left_child = left_subarray[0]
        # 현재 root의 왼쪽에 left_child를 연결
        딕셔너리[root][0] = left_child
        # 그리고 그 왼쪽 자식에 대해 똑같은 작업을 하러 재귀 호출
        dfs(left_subarray, 딕셔너리)

    # 오른쪽 자식이 실제로 존재하면
    if right_subarray:
        right_child = right_subarray[0]
        # 현재 root의 오른쪽에 right_child를 연결
        딕셔너리[root][1] = right_child
        # 그리고 그 오른쪽 자식에 대해 똑같은 작업을 하러 재귀 호출
        dfs(right_subarray, 딕셔너리)

def post_order(graph, node, answer):
    if node == ".":
        return

    post_order(graph, graph[node][0], answer)
    post_order(graph, graph[node][1], answer)
    answer.append(node)



# --- 메인 코드 ---
import sys

sys.setrecursionlimit(10 ** 6)

preorder_list = []
adj_graph = {}
answer = []

try:
    preorder_list = [int(line.strip()) for line in sys.stdin]
except ValueError:
    pass

for element in preorder_list:
    adj_graph[element] = [".", "."]

# 수정 5: 함수 호출 방식을 변경된 파라미터에 맞게 수정
if preorder_list:
    dfs(preorder_list, adj_graph)

# preorder_list가 비어있지 않은 경우에만 실행 (중요!)
if preorder_list:
    root_node = preorder_list[0]
    post_order(adj_graph, root_node, answer)

for i in answer:
    print(i)