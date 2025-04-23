import sys
N, K = map(int,sys.stdin.readline().split())
l =list(map(int,sys.stdin.readline().split()))
check = []
num = sum(l[:K])
check.append(num)
for i in range(0,N-K):
    num-=l[i]
    num+=l[i+K]
    check.append(num)
print(max(check))
