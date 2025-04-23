# def solution(land):
#     dr = [0,-1,0,1]
#     dc = [-1,-0,1,0]
#     max_val = 0
#     def dfs(j,i,visited):
#         size = 1
#         visited.add(j,i)
#         for i in range(4):
#             nr, nc = j + dr[d], i + dc[d]
#             if 0<= nr <= len(land[0]) and 0<= nc<=len(land) and land[j+dr[i]][i+dc[i]] == 1 and (nr,nc) not in visited:
#                 dfs(j+dr[i],i+dc[i],visited)
#     for i in range(len(land[0])):
#         visited = set()
#         for j in range(len(land)):
#             if land[j] == 1 and (j,i) not in visited:
#                 dfs(j,i,visited)
#         max_val = max(max_val,)
#         print(visited)
#     return max_val

# [[0, 0, 0, 1, 1, 1, 0, 0],
#  [0, 0, 0, 0, 1, 1, 0, 0],
#  [1, 1, 0, 0, 0, 1, 1, 0],
#  [1, 1, 1, 0, 0, 0, 0, 0],
#  [1, 1, 1, 0, 0, 0, 1, 1]]
import sys

limit_number = 10000
sys.setrecursionlimit(limit_number)
from collections import deque


def solution(land):
    dr = [0, -1, 0, 1]
    dc = [-1, 0, 1, 0]
    max_val = 0

    def dfs(j, i, visited):
        group_j = j
        group_i = i
        dq = deque([(j, i)])
        while dq:
            j, i = dq.popleft()
            if (j, i) not in visited:
                visited.add((j, i))
                land[j][i] = (group_j, group_i)
                for d in range(4):
                    nr, nc = j + dr[d], i + dc[d]
                    if 0 <= nr < len(land) and 0 <= nc < len(land[0]) and land[nr][nc] == 1 and (nr, nc) not in visited:
                        dq.append((nr, nc))

    check_group = dict()
    for i in range(len(land[0])):
        size = 0
        for j in range(len(land)):
            visited = set()  # 열별로 방문 관리
            if land[j][i] == 1 and (j, i) not in visited:
                dfs(j, i, visited)
                check_group[(j, i)] = len(visited)
        check_visited = []
        for k in range(len(land)):
            if check_group[(k, i)] and (k, i) not in check_visited:
                size += check_group[(k, i)]
                check_visited.append((k, i))
        max_val = max(max_val, size)

    return max_val


[[0, 0, 0, (0, 3), (0, 3), (0, 3), 0, 0],
 [0, 0, 0, 0, (0, 3), (0, 3), 0, 0],
 [(2, 0), (2, 0), 0, 0, 0, (0, 3), (0, 3), 0],
 [(2, 0), (2, 0), (2, 0), 0, 0, 0, 0, 0],
 [(2, 0), (2, 0), (2, 0), 0, 0, 0, (4, 6), (4, 6)]]

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))


