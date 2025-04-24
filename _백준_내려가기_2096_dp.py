import sys
input = sys.stdin.readline
# N 줄에 0~9 까지 숫자가 세 개씩 적혀있음
# 첫 째줄에서 시작해서 마지막 줄까지 가면 끝

# 처음에는 적혀있는 세 숫자중 하나 선택해서 시작하여 다음줄로 내려감
# 다음줄로 갈때 제약조건
# 바로 아래수로 가거나, 바로 아래수와 붙어 있는 수로만 갈 수 있음
#이때 얻을 수 있는 최대 점수와 최소 점수

N = int(input())
# 첫 번째 줄은 따로 입력 받음
matrix = [list(map(int,input().split()))]
# 입력받은 첫번째줄에서 해당 인덱스의 최소, 최대값을 지정(메모리를 효율적으로 관리하기위해 최소값, 최대값을 같이 관리)
prev_dp = [[matrix[0][i],matrix[0][i]] for i in range(3)]
for i in range(N-1):
    # 메모리 제한 때문에 for문을 돌면서 입력받은 값을 바로 처리
    # a,b,c는 새로 계단을 내려갈때 선택되는 값
    a,b,c = list(map(int,input().split()))
    # 각 인덱스의 0번째 값은 최소값, 1번째 값은 최대값
    # 해당 인덱스에서 선택될 수 있는 값은 
    # 최소값의 경우 
    # 0일떄는 이전값 0,1 값중 최소값 + a
    # 1일때는 이전값 0,1,2 중 최소값 + b
    # 2일때는 이전값 1,2 중 최소값 + c
    prev_dp[0][0],prev_dp[1][0],prev_dp[2][0] = min(prev_dp[0][0],prev_dp[1][0]) + a,min(prev_dp[0][0],prev_dp[1][0],prev_dp[2][0]) + b,  min(prev_dp[1][0],prev_dp[2][0]) + c
    # 최대값의 경우 
    # 0일떄는 이전값 0,1 중 최대값 + a
    # 1일때는 이전값 0,1,2 중 최대값 + b        
    # 2일때는 이전값 1,2 중 최대값 + c  
    prev_dp[0][1],prev_dp[1][1],prev_dp[2][1] = max(prev_dp[0][1],prev_dp[1][1]) + a,max(prev_dp[0][1],prev_dp[1][1],prev_dp[2][1]) + b,max(prev_dp[1][1],prev_dp[2][1]) + c
# 마지막 줄에서 최대값과 최소값을 출력
print(max(prev_dp[0][1],prev_dp[1][1],prev_dp[2][1]),min(prev_dp[0][0],prev_dp[1][0],prev_dp[2][0]))