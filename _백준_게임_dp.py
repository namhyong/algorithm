# N*M의 보드가 있음
# 1~9 까지 숫자,구멍으로 보드가 채워져 있음
# 가장 왼쪽에 동전 올려 놓기
# 동전 움직이는 방식
# 1. 동전 있는 곳에 쓰였는 숫자 X보기
# 2. 위 아래 왼쪽 오른쪽 중 하나를 고름
# 3. 동전을 고른 방향으로 X만큼 움직임 이때 있는 구멍은 무시
# 만약 동전이 구멍에 가거나 숫자보다 크다면 게임 종료, 가능한 오래 하고 싶음
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def dfs(x, y):
    if dp[x][y]:  # 이미 방문해서 계산된 값이면 그대로 반환
        return dp[x][y]
    if visited[x][y]:  # 사이클(무한 루프)이 발생하면 -1 출력 후 종료
        print(-1)
        exit()
    visited[x][y] = 1
    move = 1
    k = int(arr[x][y])
    for i in range(4):
        nx, ny = x + dr[i] * k, y + dc[i] * k
        if not (0 <= nx < N and 0 <= ny < M):  # 보드 밖으로 나가면 continue
            continue
        if arr[nx][ny] == "H":  # 구멍을 만나면 continue
            continue
        move = max(move, dfs(nx, ny) + 1)
    visited[x][y] = 0  # 탐색 완료 후 방문 해제
    dp[x][y] = move
    return dp[x][y]
print(dfs(0, 0))
# dfs로 step들어갈때마다 move 값은 1임 그리고 최대 깊이 들어가면서 이전 스탭으로 빠져나올 때 +1 해주고 move값을 갱신 함
# 그리고 for문을 돌리면서 현재 스탭에서 더 들어갈 수 있는 다음 스탭이 있는지 찾고 있다면 그친구도 dfs해줌
# 이후 그친구 빠져나오면서 현재 step에서 찾을 수 있는 최대 move값을 갱신해주는 느낌
# 이와중에 dp에 이미 저장되어 있는 값이 있다면 해당 위치는 이미 계산한 값이 거기에 저장되어 있는거기 때문에 스탭을 진행해주지 않고 바로 최대값 반환
# 그리고 스탭을 진행하다가 visited가 1인데를 다시 방문한거면 dfs돌다가 같은데 방문된거기 때문에 그 루트로만 가면 무한 루프가 되기 때문에 바로 -1반환
# 그게 아니라면 dfs 빠져 나오면서 visited 해재해주는거임 다른 루트로 해당 노드를 방문하면 무한루프가 아닐수 있기 때문에
# 
# [[5, 1, 0, 4, 0, 1, 1],
#  [0, 0, 0, 0, 0, 0, 0],
#  [1, 0, 0, 3, 1, 0, 2]]
# move = 3
# [[5, 1, 0, 4, 0, 1, 1],
#  [0, 0, 0, 0, 0, 0, 0],
#  [1, 0, 0, 3, 1, 0, 2]]
#
# [[0, 0, 0, 1, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0],
#  [1, 0, 0, 1, 0, 0, 0]]
