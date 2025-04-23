# T = int(input())
# for _ in range(T):
#     N = int(input())
#     a, b = 1, 0 # 0과 1이 호출된 횟수
#     for i in range(N):
#         # 0은 1이 호출된 횟수만큼, 1은 0과 1이 호출된 합만큼 출력됨
#         a,b = b, a+b
#     print(a,b)
# # 2 -> 1/1
# # 3 -> 1/2
# # 4 -> 2 3 -> 0 1 / 1 2-> 0 1 --> 2/3


# dp
T = int(input())
for _ in range(T):
    N = int(input())
    dp = [[]]*41
    dp[0] = [1,0]
    dp[1] = [0,1]
    dp[2] = [1,1]
    for i in range(3,N+1):
        dp[i] = [dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]]
    # print(dp)
    print(*dp[N])
