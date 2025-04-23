# 민식이는 회사의 중요 뉴스를 모두에게 전달
# 회사는 트리구조
# 모든 직원은 정확하게 한 명의 직속 상사가 있음
# 자기 자신은 직접상사나 간접 상가가 아님
# 모든 직원은 민식이의 직접 혹은 간접 부하임 (민식이 1짱)
# 1. 민식이는 자기 직접 부하에게 한 번에 하나씩 전화하여 뉴스 전달
# 2. 뉴스를 들은 부하들은 자기 직접 부하에게 한 번에 하나씩 전달
# 3. 모든 사람이 전화를 들을때 까지 하고, 모든 사람은 자기 직속 부하에게만 전화 가능
# 모든 직원이 뉴스를 들을때 걸리는 최소 시간
# 민식이는 사원번호 0이고, 다른사람은 1번부터 시작


# import sys
# input = sys.stdin.readline
#
# # 직원의 수
# N = int(input())
#
# # 자기 상사 번호 0번째는 민식이 자기 자신이라 -1
# boss_num = list(map(int,input().split()))
# tree = [[]for _ in range(N)]
# for emp_num,boss in enumerate(boss_num[1:]):
#     tree[boss].append(emp_num+1)
# print(tree)
# # visited를 만들고 모든 수 즉, len(visited가 N이랑 같으면 종료)
# # recursion을 이용해서 계속 재귀 해서 어떤 숫자에서 시작해야 가장 큰지를 결정
# dp = [0]*N
# print(dp)
# def dfs(a, check):
#     dp[a] = len(tree[a])+check
#     if not tree[a]:  # 더 이상 부하가 없으면 현재 check 반환
#         return check
#     for i in tree[a]:
#         dfs(i, check + 1)
# # [4] -> [5] ->[] -> [] -> []
# # X개가 들어왔어 X시간이 걸린다고 생각해 일단 그러고 다음뎁스로 넘어가면서 1초를 증가시켜
# # 그러면 check가 1이 늘어날거야
# # 다음 뎁스로 가서 현재 보내야되는 애들과 이전에 모아왔던 시간들을 더해
# # 반복해서 뎁스가 깊어질수록 1씩 늘기 때문에 중간에 많이 보내야 되는 애들이 있더라도 뎁스가 늘면서 따라잡힐수도 있음
#
# # 현재 시간에서 보내야하는 개수랑 개수
# print(dfs(0,0))
# print(dp)
# 뒤에 얘기해야할 사람이 많은 사람이 먼저 시작하는게 이득임
# 뒤에 얘기할 사람이 많은 사람을 저장
# 15
# -1 0 0 0 0 2 2 3 3 6 7 7 4 12 13
# 1
# 2 5
# 2 6 9
# 3 7 10
# 3 7 11
# 3 8
# 4 12 13 14 15

# 1 3 8 17
# 1 3 9
# 1 4 10
# 1 4 11
# 1 5 12 18
# 1 5 13 19
# 2 6 14 20
# 2 7 15
# 2 7 16 21 22 23
# 1초: 0->2번
# 2초: 0->1번, 2->7번
# 3초: 1->5번,2->6번,7->16번
# 4초: 1->3번,5->12번,6->14번,7->15번,16->21번
# 5초: 1->4번,3->8번,5->13번,12->18번,14->20번,16->22번
# 6초: 13->19번, 4번-> 10번,13->19번, 8번->17번,22번->23번
# 7초: 4->11번


import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 직원의 수
N = int(input())

# 자기 상사 번호 리스트 입력
boss_num = list(map(int, input().split()))

# 트리 구조 생성
tree = [[] for _ in range(N)]
for emp_num, boss in enumerate(boss_num[1:], start=1):
    tree[boss].append(emp_num)


# DFS 구현
def dfs(node):
    times = []  # 각 부하 직원의 뉴스 전달 시간 저장 리스트

    for child in tree[node]:
        times.append(dfs(child))  # 재귀적으로 부하 직원들의 전달 시간 계산

    if not times:  # 부하가 없는 경우, 전달 시간 0
        return 0
    print(times)
    # 가장 많은 시간이 걸리는 직원이 우선적으로 전화를 받아야 하므로 내림차순 정렬
    times.sort(reverse=True)

    # 최적의 전파를 위해 부하 직원들이 동시에 전화할 수 있도록 계산
    max_time = 0
    for i, t in enumerate(times):
        max_time = max(max_time, t + i + 1)  # i는 동시에 전화하는 효과를 반영

    return max_time


# 0번 직원(민식이)부터 시작
print(dfs(0))
