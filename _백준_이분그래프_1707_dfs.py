
# 테케 개수 K개
# 각 테케 첫째줄에는 정점 개수 V와 간선 개수 E가 빈칸을 두고 입력
# 각 정점은 1~ V까지 존재
# 각 줄에는 두 정점 번호 u,v가 존재
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

T = int(input())

def dfs(node, group):
    global flag
    visit[node] = group
    for neighbor in arr[node]:
        if visit[neighbor] == 0:
            dfs(neighbor, 3 - group)
        elif visit[node] == visit[neighbor]:
            flag = 0
            return

for _ in range(T):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V + 1)]
    visit = [0] * (V + 1)
    flag = 1

    for _ in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    for i in range(1, V + 1):
        if visit[i] == 0 and flag:
            dfs(i, 1)

    if flag:
        print('YES')
    else:
        print('NO')