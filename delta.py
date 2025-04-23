# dr = [0,1,0,-1]
# dc = [1,0,-1,0]
# #테스트 케이스 갯수가 들어오고 그만큼 테스트를 반복한다
# for tc in range(1, int(input())+1):
# # N * N 행렬임을 명시하여 행렬의 크기를 나타낸다
#     N = int(input())
# # 주어진 미로를 이차원 리스트 화 하여 행렬을 만든다
#     miro = [list(map(int,input())) for _ in range(N)]
#     stack = []
#     visited = []
#     answer = 0
#     for startR in range(N):
#         for startC in range(N):
#             if miro[startR][startC] == 2:
#                 stack.append([startR,startC])
#                 break
#     while stack:
#         r, c = stack.pop()
#         visited.append((r,c))
#         for i in range(4):
#             nr = r +dr[i]
#             nc = c +dc[i]
#             # 우, 하, 좌, 상 순서
#             if 0<= nr < N and 0 <= nc <N and (nr,nc) not in visited:
#                 if miro[nr][nc] == 0 :
#                     stack.append([nr,nc])
#                 elif miro[nr][nc] == 3:
#                     stack.append([nr,nc])
#                     answer = 1
#                     break
#     print(f'#{tc} {answer}')


dr = [1,-1,0,0]
dc = [0,0,1,-1]
def DFS(r, c):
    global cnt
    arr[r][c] = 0
    cnt+=1
    for i in range(4):
        nr = r+ dr[i]
        nc = c+ dc[i]
        # 행이나 열을 넘어가면 continue로 루프 다시 돌게 함
        if nr<0 or nr >= N or nc <0 or nc>=N:
            continue
        if arr[nr][nc] == 0:
            continue
        DFS(nr,nc)

N = int(input())
arr = [list(map(int,input())) for _ in range(N)]

# 이중 for 문으로 행 열, 순회 하다가 1 만나면 cnt 0으로 초기화 하고, 사방탐색 시작
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt = 0
            DFS(i,j)
            print(cnt)
# 7
# 0000011
# 0000000
# 0011100
# 0010111
# 0110010
# 0011100
# 0000000