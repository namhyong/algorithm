import sys
import heapq
input =sys.stdin.readline

V,E = map(int,input().split())
mat = [[] for _ in range(V+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    mat[a].append((c,b))
    mat[b].append((c,a))
heap = [(0,1)]
visited = set()
total_cost = 0
while heap:
    cost,node = heapq.heappop(heap)
    if node not in visited:
        visited.add(node)
        total_cost+=cost
        for i in mat[node]:
            heapq.heappush(heap,i)
print(total_cost)