# DFS, BFS 기초

from collections import deque


def DFS(graph, root, visited):
    visited[root] = True
    print(root, end=' ')

    for i in graph[root]:
        if not visited[i]:
            DFS(graph, i, visited)


def BFS(graph, root, visited):
    hip = deque([root])
    visited[root] = True

    while hip:
        pick = hip.popleft()
        print(pick, end=' ')
        for i in graph[pick]:
            if not visited[i]:
                hip.append(i)
                visited[i] = True


visited = [False]*9
graph_list = [[],
              [2, 3, 8],
              [1, 7],
              [1, 4, 5],
              [3, 5],
              [3, 4],
              [7],
              [2, 6, 8],
              [1, 7]
              ]
# DFS(graph_list, 3, visited)
BFS(graph_list, 1, visited)
