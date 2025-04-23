# V,E = map(int,input().split())
# list = [[] for _ in range(V+1)]
#
# for _ in range(E):
#     start, end = map(int, input().split())
#     list[start].append(end)
#     list[end].append(start)
#
# stack = [1]
# visited = []
#
# while stack:
#     current= stack.pop()
#     if current not in visited:
#         visited.append(current)
#     for destination in list[current]:
#         if destination not in visited:
#             stack.append(destination)
# print(visited)

# V,E = map(int,input().split())
# l = [[0]*(V+1) for _ in range(V+1)]
#
# for _ in range(E):
#     start, end = map(int, input().split())
#     l[start][end] = 1
#     l[end][start] = 1
#
# stack = [1]
# visited = []
#
# while stack:
#     current= stack.pop()
#     if current not in visited:
#         visited.append(current)
#     for destination in range(V+1):
#         if l[current][destination] and destination not in visited:
#             stack.append(destination)
# print(*visited)

# def dfs(n):
#     if n not in visited:
#         visited.append(n)
#     for destination in range(V+1):
#         if l[n][destination] and destination not in visited:
#             dfs(destination)
#
# V, E = map(int, input().split())
# l = [[0]*(V+1) for _ in range(V+1)]
# for _ in range(E):
#     start ,end = map(int,input().split())
#     l[start][end] = 1
#     l[end][start] = 1
#
# visited=[]
#
# dfs(1)
# print(*visited)

# 7 8
# 1 2
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7
V,E = map(int,input().split())
adj_list = [[]*(V+1) for _ in range(V+1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_list[start].append(end)
    adj_list[end].append(start)

stack = [1]
visited = []
while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)

        for destination in adj_list[current]: #for 루프 돌면서 지금 방문한 노드랑 연결되어 있는 노드들을 모두 stack애 넣음
            if destination not in visited: # 1을 생각하면, adj_list[1]의 이차원 리스트에는 2,3 이 있고, 2,3은 모두 visited에 없으니
                                            # stack에 넣고 다음 current로 넘어가서 stack pop을 하면 3이 pop됨
                stack.append(destination)
print('이동경로', *visited)
# [[2,3],[1,4,5],[1,7],[2,6],[2,6],[4,5,7],[6,3]]
# -> 1: stack = [2,3]
# -> 3: stack = [2] -> 1은 visited ,7 append -> [2,7]
# -> 7: stack = [2] -> 3은 visited ,6 append -> [2,6]
# -> 6: stack = [2] -> 7은 visited ,4,5 append -> [2,4,5]
# -> 5: stack = [2,4] -> 6은 visited, 2 append -> [2,4,2]
# -> 2: stack = [2,4] -> 1,5는 visited, 4 append -> [2,4,4]
# -> 4: stack = [2,4] -> 2,6 visited -> [2,4]
# 나머지 2,4는 모두 visted여서 stack 끝 while 종료
# 따라서, 1-3-7-6-5-2-4 순서 방문


print(1//2)