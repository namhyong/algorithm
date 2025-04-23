from itertools import combinations
N,M = map(int,input().split())
num = []
sel = [0 for _ in range(M)]
ans = set()
for i in range(1,N+1):
    num.append(i)
def combination(idx, sidx):
    if sidx == M:
        print(*sel)
        return

    if idx == N:
        return

    sel[sidx] = num[idx]
    combination(idx+1, sidx+1)
    combination(idx+1, sidx)


combination(0, 0)

# comb = combinations(num,M)
# for i in comb:
#     print(*i)