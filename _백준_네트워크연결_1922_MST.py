import sys
input = sys.stdin.readline
def find_set(x):
    # 자기 자신으로 초기화 한 parent 배열에서 자기 자신이 아니라면 이미 다른 부모노드로 바뀐것이기 때문에, 그 해당 노드가 최상위 노드인지
    # 확인하기 위해 find_set 재귀
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    # 같다면 해당 노드의 최상위 노드를 return 해줌
    return parent[x]
def union(a,b):
    # 각 노드별 최상위 부모를 찾는 과정
    x =find_set(a)
    y = find_set(b)
    # 만약 최상위 부모가 큰쪽에 노도의 값을 다른 값으로 바꿈
    if y <x:
        parent[x] = y
    else:

        parent[y] = x
N = int(input())
M = int(input())
parent = list(range(N+1))
edges = [list(map(int,input().split())) for _ in range(M)]
edges.sort(key=lambda x:x[2])
total_cost = 0
for a,b,c in edges:
    # 최상위 부모를 찾기위한 find_set
    if find_set(a) != find_set(b):
        # 둘의 부모가 다르다면, 간선을 연결하여 간선 비용 올라감
        total_cost+=c
        #둘의 부모를 합쳐주는 과정이 필요
        union(a,b)
print(total_cost)

# [0,1,2,3,4,5,6]
# [[2, 3, 2], [4, 5, 3], [1, 3, 4], [1, 2, 5], [3, 4, 6], [2, 4, 7], [4, 6, 8], [5, 6, 8], [3, 5, 11]]
# 2 3 -> find_set(2),find_set(3) -> 2,3 리턴-> 다르기 때문에 cost올리고 union과정-> 2<3이기 때문에 parent[3] =2 [0, 1, 2, 2, 4, 5, 6]
# 4 5 -> find_set -> 4,5 -> cost+=c,union->paent[5] = 4 [0,1,2,2,4,4,6]
# 1 3 -> find_set(1),find_set(3)->find_set(2)->1,2리턴 ->parent[2] = 1 [0,1,1,2,4,4,6]
# 1 2 -> 1,1 리턴 다음스탭
# 3 4 -> 1,4 리턴 -> parent[4]= 1 -> [0,1,1,2,1,5,6]
# 2 4 -> 1 1 리턴 continue
# 4 6 -> 1,5 리턴 parent[6] = 1 -> [0,1,1,2,1,5,1]
# 5 6 -> 5 1 리턴 parent[5] = 1 -> [0,1,1,2,1,1,1]
# 3 5 -> 1 1 리턴