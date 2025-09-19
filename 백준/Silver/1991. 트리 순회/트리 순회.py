def 전위순회(graph, node):
    visited.append(node)
    for adj_node in graph[node]:
        if adj_node == '.':
            continue

        전위순회(graph, adj_node)

def 중위순회(graph, node):
    if graph[node][0] == ".":
        pass
    else:
        중위순회(graph, graph[node][0])

    visited.append(node)

    if graph[node][1] == ".":
        pass
    else:
        중위순회(graph, graph[node][1])

def 후위순회(graph, node):
    for adj_node in graph[node]:
        if adj_node == '.':
            continue
        후위순회(graph, adj_node)

    visited.append(node)



N = int(input())
adj_graph = {}
visited = []

# 일단 연결 리스트로 만들자.
for i in range(N):
    row = input().split()
    adj_graph[row[0]] = []
    for j in range(1, len(row)):
        adj_graph[row[0]].append(row[j])

visited = []
전위순회(adj_graph, 'A')
print("".join(visited))

visited = []
중위순회(adj_graph, 'A')
print("".join(visited))

visited = []
후위순회(adj_graph, 'A')
print("".join(visited))