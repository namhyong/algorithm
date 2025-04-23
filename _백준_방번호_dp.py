import sys
# 문방구에서 파는 숫자는 0 ~ N-1
N = int(sys.stdin.readline())
# 각 숫자 i의 가격
P = list(map(int,sys.stdin.readline().split()))
# 숫자를 구매하기 위해 준비한 돈
M = int(sys.stdin.readline())
# 숫자들의 연결로 만들 수 있는 가장 큰 수 구하기
dp = [-float("inf") for _ in range(M+1)]
# 가장 큰 수 부터 역순으로 확인
for i in range(N-1,-1,-1):
    # 가장 큰 수 가격 ~ 0원 짜리까지
    p = P[i]
    # i 수를 산다고 가정하기 때문에 그 다음에 쓸 수 있는 비용으로 찾기
    for j in range(p, M+1):
        # 현재 방 번호, 현재 인덱스, 현재 가격 - p 에 p로 살 수 있는 방 번호를 붙인 값 중 큰 값
        dp[j] = max(dp[j], i, dp[j-p]*10 + i)
        # print(dp[j])
# print(dp)
print(dp[M])