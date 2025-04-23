# 빙산이 양의 정수
# 이외에 바다는 0
# 빙산의 높이는 바다와 많이 접해있을 수록 빨리 녹는다
# 빙산의 개수는 일년마다 동서남북으로 붙어있는 0의 칸 수만큼 줄어든다
# 각 칸은 0보다 더 줄어들지는 않는다
# 한 덩어리의 빙산이 두 덩어리 이상으로 분리되는 최소 시간

# 첫줄 행렬 N,M
# 2줄부터 빙산 정보 들어옴 빙산은 0~10 이하

# for 문을 돌려서 숫자가 나오면 사방탐색을 해서 주변 0 수를 찾고 숫자를 줄임
# 그다음 dfs 사방탐색 으로 모든 빙산들이 연결되어 있는지 확인
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
N,M = map(int,input().split())

ice_berg = [list(map(int,input().split())) for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
check_time = 0


def dfs(r, c):
    if (r, c) in now_ice_berg:
        now_ice_berg.remove((r, c))
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N or 0 <= nc < M:
            if (nr, nc) in visited or not ice_berg[nr][nc]:
                continue
            else:
                visited.append((nr, nc))
                dfs(nr, nc)
while True:
    # check_visited = []
    check_ice_berg = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not ice_berg[i][j]:
                continue
            else:
                check_ice_berg[i][j] = ice_berg[i][j]
                # check_visited.append((i,j))
                for k in range(4):
                    nr = i+dr[k]
                    nc = j+dc[k]
                    if 0<=nr<N or 0 <=nc <M :
                        if check_ice_berg[i][j]>0 and ice_berg[nr][nc] == 0:
                            check_ice_berg[i][j]-=1
    ice_berg = check_ice_berg
    visited = []
    now_ice_berg = []
    for i in range(N):
        for j in range(M):
            if ice_berg[i][j]:
                now_ice_berg.append((i,j))
    for i in range(N):
        for j in range(M):
            if ice_berg[i][j]:
                dfs(i,j)
                break
    if not now_ice_berg:
        break
    else:
        check_time+=1
print(check_time)



# [[0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 1, 4, 1, 0, 0],
#  [0, 0, 0, 1, 5, 0, 0],
#  [0, 4, 4, 1, 2, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0]]

