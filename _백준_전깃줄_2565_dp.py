import sys
input= sys.stdin.readline
N = int(input())
lines = [list(map(int,input().split())) for _ in range(N)]
lines.sort()
dp = [1] * N
# 총 전깃줄 중 안전한 전기줄들만 골라서 저장
# a 숫자를 오름차순으로 정렬하고 b숫자가 이전에 비교하는 b숫자들보다 크면 안전한 전깃줄
# 비교한 전기줄의 안전한 전깃줄 수+현재 자신 과 현재 자신이 가진 안전한 전깃줄 중 큰 수를 dp에 저장
# 총 전깃줄에서 안전한 전깃줄을 빼면 제거해야하는 전깃줄 수가 나옴
for i in range(1,N):
    for j in range(0,i):
        if lines[j][1]< lines[i][1]:
            dp[i] = max(dp[i],dp[j]+1)
print(N-max(dp))
