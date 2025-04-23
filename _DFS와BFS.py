from collections import deque

# 입력 처리
N, M, V = map(int, input().split())
l_dfs = [[] for _ in range(N + 1)]
l_bfs = [[] for _ in range(N + 1)]

# 간선 입력
for _ in range(M):
    start, end = map(int, input().split())
    l_dfs[start].append(end)
    l_dfs[end].append(start)  # 무방향 그래프일 경우
    l_bfs[start].append(end)
    l_bfs[end].append(start)  # 무방향 그래프일 경우

# 정점 번호 오름차순 정렬
for i in range(1, N + 1):
    l_dfs[i].sort()
    l_bfs[i].sort()

# DFS 함수
def dfs(start):
    visited = []
    stack = [start]

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            stack.extend(sorted(l_dfs[v], reverse=True))
    return visited

# BFS 함수
def bfs(start):
    visited = []
    dq = deque([start])

    while dq:
        v = dq.popleft()
        if v not in visited:
            visited.append(v)
            dq.extend(l_bfs[v])
    return visited

# DFS와 BFS 결과 출력
dfs_result = dfs(V)
bfs_result = bfs(V)
print(*dfs_result)
print(*bfs_result)
