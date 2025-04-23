# 늘리기 위한 고객 C
# 도시 개수 N
# X원 들이서 Y명 늘릴수 있음
# 2X원이면 2Y명, 3X원이면 3Y명으로 정수배로 늘지만, X/2원으로 Y/2명 이런식으로 늘릴수는 없음

import sys
input  = sys.stdin.readline
C,N = map(int,input().split())
l = [list(map(int,input().split()))  for _ in range(N)]
dp = [float('inf') for _ in range(C+100)]
dp[0] = 0
l.sort()
# 11 3 1
# 일단 customer 별로 만들수 있는 cost를 쫙 설정해 놓고
# 다음 customer cost 세트가 왔을 때
# 다음 코스트로 만들수 있는 customer 수 를 뺀 이전 값에 현재 세트의 cost값을 더해서
# dp[i]위치에 지금 세트+이전 세트 더해서 만든 비용이랑 기존에 구해놨던 값중에 작은 값으로 업데이트 함
#이런식으로 해서 최적값 구하기
for cost,customer in l:
    for i in range(customer,C+100):
        dp[i] = min(dp[i - customer] + cost, dp[i])
print(min(dp[C:]))
