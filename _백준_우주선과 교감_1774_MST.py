# 우주신과의 교감
import math
import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())


def prim(start):
    result = 0
    visited = [False] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if visited[node]:
            continue
        visited[node] = True
        result += dist
        for ndist, nnode in arr[node]:
            heapq.heappush(q, (ndist, nnode))
    return result


# 노드 위치 정보
nodes = [[]]
for _ in range(N):
    nodes.append(list(map(int, input().split())))

# 이미 연결되어 있는 값을 저장
connected = set()
for _ in range(M):
    x, y = map(int, input().split())
    connected.add((x, y))
    connected.add((y, x))

# 연결리스트
# 한 노드에서 갈 수 있는 모든 노드를 계산하기 위해 2중 for문 사용
# 입력으로들어온 노드가 0이아닌 1부터 시작하기 때문에 계산하기 위해서 1부터 시작
arr = [[] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(i+1, N+1):
        # 이미 연결되어 있다면 dist를 0으로
        if (i, j) in connected:
            arr[i].append((0, j))
            arr[j].append((0, i))
            continue
        # 연결 되지 않았다면
        # 거리 계산, 노드와 노드를 이으려면 좌표 평면에서 가로 거리와 세로 거리를 알면 직선 거리를 구할 수 있음
        # 유클리디안 거리로 피타고라스를 이용하여 구함 가로 제곱에 세로 제곱을 더하고 루트(제곱근)을 구하는 방식
        dist = math.sqrt((nodes[i][0]-nodes[j][0])**2 + (nodes[i][1]-nodes[j][1])**2)
        # 이렇게 생긴 가중치 거리를 이용하여 그래프를 구성
        arr[i].append((dist, j))
        arr[j].append((dist, i))
print("%.2f" % prim(1))