import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
N = int(input())

map = [list("".join(input().rstrip())) for _ in range(N)]
dr = [1,-1,0,0]
dc = [0,0,1,-1]

# 적록 색약 아닌경우 체크
check_a = [[0]*N for _ in range(N)]
# 적록 색약인 경우 체크
check_b = [[0]*N for _ in range(N)]
# 초록색을 빨간색으로 바꾼 map_b
map_b = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if map[i][j] == "G":
            map_b[i].append("R")
        else:
           map_b[i].append(map[i][j])

# 적록색약이 아닌경우 같은 색을 찾는 dfs
def dfs_a(r,c,prev_color):
    # 범위를 넘어가거나 색이 다른 경우 return 예외처리
    if not 0<=r<N or not 0<=c<N or map[r][c] != prev_color:
        return
    # 이미 방문한 곳이라면 다시 방문 하지 않도록 return
    if check_a[r][c]:
        return
    # 현재 도착한 지역을 방문 처리
    else:
        check_a[r][c] =1
    # 사방 탐색
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        dfs_a(nr,nc,map[r][c])
    return

# 적록색약인 경우 G를 R로 바꾼 map을 탐색하는 dfs
def dfs_b(r,c,prev_color):
    if not 0<=r<N or not 0<=c<N or map_b[r][c] != prev_color:
        return
    if check_b[r][c]:
        return
    else:
        check_b[r][c] =1
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        dfs_b(nr,nc,map_b[r][c])
# 각각의 군집 기록
a_check = 0
b_check = 0

# dfs 돌때마다 방문한 곳은 check_a,check_b에 기록하여 방문한 곳을 다시 방문 안하게 처리하고
# 방문하지 않은 지역 즉, check_a,check_b가 0인 지역은 다시 dfs 들어감
# dfs가 끝나고 빠져나온경우 군집 탐색이 끝난것이기 때문에 군집의 개수 하나 올림
for i in range(N):
    for j in range(N):
        if not check_a[i][j]:
            dfs_a(i,j,map[i][j])
            a_check+=1
        if not check_b[i][j]:
            dfs_b(i,j,map_b[i][j])
            b_check+=1
print(a_check,b_check)