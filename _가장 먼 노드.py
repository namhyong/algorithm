from collections import deque
def solution(n, edge):
    check = [999 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for v1,v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)
    q = deque([(1,0)])
    visited = [0 for _ in range(n+1)]
    while q:
        current, weight = q.popleft()
        if not visited[current]:
            visited[current] = 1
            for i in graph[current]:
                if not visited[i]:
                    q.append((i,weight+1))
        if check[current] > weight:
            check[current] = weight
    return check.count(max(check[1:]))

print(solution(4, [[3, 4], [1, 3], [2, 3], [2, 1]]))