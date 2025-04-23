from collections import deque
def BFS(r,c):
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    q = deque([(r,c)])
    visited = []
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i],c+dc[i]
            visited.append((nr,nc))
            if 0<=nr<N and 0 <=nc < M and arr[nr][nc] != 0:
                q.append((nr,nc))
            else:
                continue



N, M= map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
BFS(0,0)
print(arr)