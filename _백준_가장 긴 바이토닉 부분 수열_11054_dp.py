# 바이토닉 수열 : 어떤 수 S를 기준으로 양쪽이 계속 작아지는 경우
# 즉, 30을 기준으로 [1,2,30,2,1], [1,2,30],[30,2,1]이 모두 바이토닉 수열
# 하지만, [30,3,1,2] 이런경우는 바이토닉 수열이 아님
# 가장 긴 바이토닉 수열의 길이를 출력
# [1,2,3,4,5,2,1] 예제의 바이토닉 수열
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
dp_to_right = [1]+[0]*N
dp_to_left = [1]+[0]*N
for i in range(1,N):
    for j in range(i-1,-1,-1):
        if A[i] >A[j]:
            if dp_to_right[i] <= dp_to_right[j]:
                dp_to_right[i] = dp_to_right[j]+1
        elif A[i] <A[j]:
            continue
        else:
            dp_to_right[i] = max(dp_to_right[j],dp_to_right[i])
A = A[::-1]
for i in range(1,N):
    for j in range(i-1,-1,-1):
        if A[i] >A[j]:
            if dp_to_left[i] < dp_to_left[j]+1:
                dp_to_left[i] = dp_to_left[j]+1
        elif A[i] <A[j]:
            continue
        else:
            dp_to_left[i] = max(dp_to_left[j],dp_to_left[i])
dp_to_left = dp_to_left[::-1]
check = 0
for i in range(len(dp_to_right)):
    c = dp_to_right[i] + dp_to_left[i]
    if check < c:
        check = c

print(check)
        # 클 때
        # 작을 때
        # 같을 때
# [1,0,0,0,0,0,0,0] -> 좌우를 구분해야 하고, 숫자별로 놓는게 좋아 보임
# 1 5 2 1 4 3 4 5 2 1
# 1 2 2
# 1 2 2 1 3
# 3 3 2 1
# 1 2 2 1 3 3 4 5
# [1,2,2,1,3,3,4,5,2,1]
# [1,5,2,1,4,3,3,3,2,1]
