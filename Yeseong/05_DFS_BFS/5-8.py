# DFS 메서드
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            

graph = [ # 각 노드에 해당하는 인덱스에는 해당 노드와 인접한 노드들의 번호가 리스트로 저장됨
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8]
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited) # 관행적으로 낮은 번호부터 시작