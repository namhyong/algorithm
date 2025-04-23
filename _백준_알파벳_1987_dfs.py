import sys

input = sys.stdin.readline

# 이동 방향 (하, 상, 우, 좌)
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

def dfs(r, c, visited, count):
    global max_count
    max_count = max(max_count, count)

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            idx = ord(board[nr][nc]) - ord('A')  # 알파벳을 인덱스로 변환
            if not visited[idx]:  # 방문하지 않은 알파벳이면 진행
                visited[idx] = True
                dfs(nr, nc, visited, count + 1)
                visited[idx] = False  # 백트래킹 (다시 원래 상태로 복구)

# 초기 상태 (0,0)에서 시작, 방문 배열을 활용
max_count = 0
visited = [False] * 26  # A~Z(26개) 알파벳 방문 여부 저장
visited[ord(board[0][0]) - ord('A')] = True  # 시작 위치 방문 체크
dfs(0, 0, visited, 1)

print(max_count)
