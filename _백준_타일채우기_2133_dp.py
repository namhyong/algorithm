# 그냥 일단 가능한 경우를 찾아보고 규칙을 찾아서 점화식 만들기
# 이 경우는 dp[i-2]*3+dp[i-4]*2+dp[i-6]*2...dp[i-j==0]*2 +2
n=int(input())
dp=[0 for i in range(n+2)]
dp[2]=3
for i in range(4,n+1,2):
        dp[i]+=dp[i-2]*3
        for j in range(i-4,-1,-2):
            dp[i]+=2*dp[j]
        dp[i]+=2
print(dp[n])