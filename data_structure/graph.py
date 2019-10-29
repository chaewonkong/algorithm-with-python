"""Graph Algorithm"""


# BFS (Breadth First Search): Queue
def bfs(graph):
    V = len(graph)
    queue = [1]
    visited = [0] * V
    visited[1] = 1

    while queue:
        v = queue.pop(0)
        print(v)
        for i in range(1, V):
            if graph[v][i] == 1 and not visited[i]:
                visited[i] = 1
                queue.append(i)
        
# DFS (Depth First Search): Stack

def connect(graph, a, b):
    graph[a][b] = 1
    graph[b][a] = 1


def dfs(graph):
    V = len(graph)
    visited = [0 for _ in range(V)]

    def search_part(here):
        print(here)
        visited[here] = 1
        for i in range(1, V):
            if graph[here][i] != 0 and not visited[i]:
                visited[i] = 1
                search_part(i)

    for i in range(1, V):
        if not visited[i]:
            search_part(i)


if __name__ == '__main__':
    graph = [[0] * 11 for _ in range(11)]

    connect(graph, 1, 2)
    connect(graph, 1, 7)
    connect(graph, 2, 3)
    connect(graph, 2, 8)
    connect(graph, 3, 4)
    connect(graph, 3, 10)
    connect(graph, 4, 5)
    connect(graph, 4, 9)
    connect(graph, 6, 7)
    connect(graph, 6, 8)
    connect(graph, 6, 9)

    # dfs(graph)
    bfs(graph)