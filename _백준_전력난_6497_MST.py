import sys
input = sys.stdin.readline
def solve(m,n):
    edges = []
    max_cost = 0
    for _ in range(n):
        x,y,z = map(int,input().split())
        edges.append((z,x,y))
        max_cost += z
    edges.sort()

    parent = [i for i in range(m)]
    def find(parent,x):
        if parent[x] != x:
            parent[x] = find(parent,parent[x])
        return parent[x]

    def union(parent,a,b):
        a = find(parent,a)
        b = find(parent,b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    res = 0
    cnt = 0
    for z,x,y in edges:
        if find(parent,x) != find(parent,y):
            union(parent,x,y)
            res += z
    print(max_cost-res)
while True:
    m,n = map(int,input().split())
    if m == 0 and n == 0:
        break
    solve(m,n)