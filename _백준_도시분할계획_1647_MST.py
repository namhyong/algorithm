import sys
import heapq
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    A,B,C = map(int,input().split())
    graph[A].append((C,B))
    graph[B].append((C,A))

def prim():
    result = []
    queue = [(0,1)]
    # 그래프를 돌면서 방문하지 않은데면 heappush 하여 heap내부에서 자동으로 최소힙이 만들어짐
    # 방문한곳을 방문 처리하고 다시 while로 가서 최소힙에서 뽑아서 가장 작은 곳이 방문한곳이면 다시 while문 방문하는식으로함
    # 이때 리스트를 만들때 heap을 사용하기 위해 그래프를 만들때 가중치를 앞에 둬야 함
    while queue:
        curr_cost,curr_node  = heapq.heappop(queue)
        if not visited[curr_node]:
            visited[curr_node] = True
            result.append(curr_cost)
            if len(result) == N:
                break
            for next_cost, next_node in graph[curr_node]:
                if visited[next_node] == False:
                    heapq.heappush(queue,(next_cost,next_node))
    return sum(result) - max(result)
print(prim())
# 2+1+2+2+1+4
# 1방문 -> 3방문 -> 2방문 -> 6방문-> 5방문->4방문->7방문
# [[],
#  [[3, 2], [2, 3], [5, 5], [2, 6]],
#  [[3, 1], [1, 3], [2, 5]],
#  [[2, 1], [1, 2], [4, 4], [6, 7]],
#  [[4, 3], [1, 6], [3, 5]],
#  [[2, 2], [5, 1], [3, 6], [3, 4]],
#  [[2, 1], [1, 4], [3, 5], [4, 7]],
#  [[6, 3], [4, 6]]]


# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4

