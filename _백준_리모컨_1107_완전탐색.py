# 특정 버튼이 고장남
# 리모컨 0~9 +,-있음 +는 현재 채널에서 +1 - 현재 채널에서 -1
# 0에서는 더 떨어지지 않음
# N채널로 이동하기 위한 버튼 최소 누르는 횟수
# 현재 채넣은 100

# 일단 예외 처리들
# 100번일때는 0
# 번호가 안망가졌을때 숫자 길이만큼 누르기 혹은 +,-로 이동이 있는데
# +-이동은 원하는 값 - 100 하고 절대값 씌우기
# 이 두 값중 작은 값
# 일단 자리수별로 비교 하는데
# 첫 값에 해당 숫자가 들어갈 수있으면 들어감
# 들어갈 수 없으면, 1 작거나 큰 수를 찾아감
# 0 인경우는 작은 값이 없으니까 큰 값
# 첫 값이 들어가지더라도, 첫값 쓴느거보다 이전값에서 1올리는게 더 작은 경우도 있음
# 예를들어 500000일때 금지 숫자가 0이라면, 511111보다 499999에서 1올리는게 더 작은 경우도 있음
# [0,1,2,3,4,5,9] -> 0 다음 스탭 ->  0 0 0 0 0 0 -> 돌아가 0 0 0 0 0 9 7번 9^6+...+9^1
import sys
input = sys.stdin.readline
# 이동하려는 번호 입력
N = int(input())
# 해당 숫자의 크기 찾기
list_N = list("".join(str(N)))
# N의 길이
len_N = len(str(N))
# 망가진 버튼 입력
M = int(input())
# 현재 번호 100번에서 망가진 번호 차이 +,-로 이동할 수 있는 크기 구함
target_diff =  abs(N-100)
# M이 0이 아닐 때문 망가진 번호들이 들어오기 때문에 if문으로 M값이 있다면 번호를 받게 처리
if M:
    # 망가진 번호 입력
    broken_num = list(map(int,input().split()))
# 망가지지 않은 번호 찾기
    not_broken_num = [i for i in range(10) if i not in broken_num]
# 0부터 숫자를 만들어서 체크할 숫자 리스트 -> 아무것도 망가지지 않았다면, 즉, not_broken_num에 숫자가 다 있다면, 0부터 99999까지 확인 가능
check = [0]*6
# 숫자를 만들었을 때 목표로 하는 번호로 이동하기 위한 차이를 기록하는 변수
low_diff = 999999
low_diff_num = 0
def dfs(target):
    # 숫자의 차이를 저장(특정 번호로 이동해서 타겟 번호로 이동할때 눌러야 하는 버튼의 수)
    global low_diff
    # 숫자의 길이를 저장(특정 번호로 이동하기 위해 이 길이 만큼 번호를 눌러야 해서)
    global low_diff_num
    # 자리수를 하나씩 늘려서 모든 자리수를 채웠을때 분기문
    if abs(target)-1 == len(check):
        # 이전 depth로 돌아가 다른 수를 찾아보기 위한 return
        return
    # 만들수 있는 모든 수를 돌며 모든 경우의 수를 탐색
    for i in not_broken_num:
        # 0이 망가졌을 때 000001=>1 이런식의 수를 채우기 위해서 뒷자리 부터 수를 채워감 이렇게 하지 않으면 한자리 수 같은것이 만들어 질 수 없음
        check[-target] = i
        # 모든 자리수를 합쳐 하나의 숫자로 만듦 예를 들어 check가[0,0,0,1,0,0]이면 100이 만들어짐
        num = int("".join(map(str, check)))
        # 만들어진 숫자와 타겟 숫자의 차이 즉, 만들어진 숫자에서 타겟 숫자가 되기 위해 +,-로 이동 해야하는 수
        diff = abs(num-N)
        # 이 diff가 기존에 찾았던 차이들 보다 작으면 현재 상황에서 가장 작은 수 이기 때문에 low_diff 업데이트 숫자 길이 low_diff_num 업데이트
        if diff< low_diff:
            low_diff = diff
            low_diff_num = num
        # 타겟 숫자와의 차이가 같을때 숫자의 길이가 더 짧은것을 선택하기 위해 숫자 크기 대소비교 작은 수가 무조건 짧거나 현재 크기와 같기 때문에
        elif diff == low_diff and low_diff_num > num:
            low_diff_num = num
        dfs(target+1)
        # dfs를 빠져나올때 헤당 자리를 다시 0으로 바꿔둠, 0이 망가진 상황에서는 00001이런것을 고려하기 힘들기 때문에 0으로 바꿔줘야 고려 가능
        check[-target] = 0

# 타겟 번호가 100이 주어지면, 현재 번호가 100이기 때문에 아무것도 하지 않음
if N == 100:
    print(0)
# 망가진 버튼이 없다면, 해당 버튼을 그냥 눌러서 이동하는거랑, +,-버튼을 눌러 이동하는 거 중 작은 값으로 출력
elif M == 0:
    # len_N: 버튼으로 눌러서 이동, target_diff: +,-로 이동
    print(min(len_N,target_diff))
# 위 상황에 해당하지 않는다면 dfs를 통해 근처값을 찾고 +,-이동 회수를 찾아 max_num에 저장하고 해당 숫자를 이동할 때 누르는 버튼 길이를 합해서
# 현재 숫자 100에서 +,-버튼으로 이동하는 수 target_diff중 대소 비교를 해서 더 작은 값을 출력
else:
    dfs(1)
    # 숫자의 길이를 저장( 해당 길이 즉,자리수 만큼 버튼을 눌러야 하기 때문)
    length = len(str(low_diff_num))
    if target_diff > low_diff+length:
        print(low_diff+length)
    else:
        print(target_diff)
# 8 주변 숫자 7,9 확인 -> 7가능 -> 다음숫자는 최대한 크게 ㄱㄱ-> 77777
# 80000
# 2
# 8 9

# 1주변 확인 0 2 ->0 가능 -> 0번으로 바꾸고 +1
# 1
# 9
# 1 2 3 4 5 6 7 8 9

# 5랑 5주변 확인 4,6 -> 5 가능 -> 다음숫자 는 비교하면서 다음 숫자랑 가깝게
# 500000
# 8
# 0 2 3 4 6 7 8 9

# 5랑 주변숫자 확인 5,4 가능 5일때는 숫자 비교 해서 숫자랑 가장 가깝게5455 혹은 9, 4일때는 최대한 크게 4999
# 5457
# 3
# 6 7 8

# 889
# 9
# 0 2 3 4 5 6 7 8 9