# 일단 가운데 까방권 하나 있음
# 친한 친구들관계도가 나오고 친구들 수가 나옴
import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int,input().split())
friends = [list(map(int,input().split())) for _ in range(M)]
count = 0
max_val = 0
friend_count = defaultdict(int)

# 친구 연결 개수 카운트
for u, v in friends:
    friend_count[u] += 1
    friend_count[v] += 1

# 정렬 (연결 개수가 적은 친구 관계가 앞에 오도록)
friends.sort(key=lambda pair: (friend_count[pair[0]] + friend_count[pair[1]], min(pair)), reverse=False)
print(friends)
# dfs로 완탐
def dfs(friend):
    for l,r  in friend:
        if l not in visited and r not in visited:
            visited.add(l)
            visited.add(r)
while count != N:
    if M == 0:
        print(1)
        break
    visited = set()
    for l,r in friends:
        if l not in visited and r not in visited:
            visited.add(l)
            visited.add(r)
    if N%2:
        if len(visited) == N-1:
            print(N)
            break
        else:
            if max_val < len(visited):
                max_val = len(visited)
            friends.append(friends.pop(0))
    else:
        if len(visited) == N:
            print(N)
            break
        else:
            if max_val < len(visited):
                max_val = len(visited)
            friends.append(friends.pop(0))
    count+=1
if count == N:
    print(max_val+1)
