import sys
import math
import heapq
input = sys.stdin.readline

n = int(input())
node = [list(map(float,input().split())) for _ in range(n)]
visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]
dis = 0
# 한 노드에서 다음 노드로 가는 거리를 계산해서 heap에 넣고 최소 비용을 계산
for i in range(n):
    for j in range(i+1,n):
        distance = math.sqrt((node[i][0]-node[j][0])**2+(node[i][1]-node[j][1])**2)
        graph[i].append((distance,j))
        graph[j].append((distance,i))

q = []
heapq.heappush(q,(0,1))
while q:
    d,i = heapq.heappop(q)
    if visited[i]:
        continue
    visited[i] = True
    dis += d
    for ndist,nnode in graph[i]:
        heapq.heappush(q,(ndist,nnode))

print(f'{dis:.2f}')