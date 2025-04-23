# import sys
# input = sys.stdin.readline
# N = int(input())
# matrix = [list(map(int,"".join(input())[:-1])) for _ in range(N)]
# # res = [1]*N^2
# res = 0
# def dfs(owner,buyer,fee):
#     for i in range(N):
#         if owner != i:
#             if i not in buyer and matrix[owner][i] >= fee:
#                 fee = matrix[owner][i]
#                 owner = i
#                 # print(fee)
#                 dfs(owner,buyer+[i],fee)
#         if i == N-1:
#             return buyer
# for i in range(N):
#     for j in range(N):
#         if i == j:
#             continue
#         else:
#             buyer = []
#             buyer.append(j)
#             owner = j
#             fee = matrix[i][j]
#             a = dfs(owner,buyer,fee)
#             print(a)
#             if len(a) > res:
#                 res = len(a)
# print(res)
# # N*N만큼 DP를 만들고 행을 찾았을때 값만큼 저장하고 다음 사는 사람있다면 넘어가기 그리고 다시 돌아와서 다른 행 볼때 기존 값으로 비교하는 형식은 어떰?
# # [[0, 2, 2], 1 ->0 번한테 2원 2번이 1번한테 2원
# #  [1, 0, 1], -> 1번이 0번한테  1원 2번이 1번한테 1원
# #  [1, 1, 0]] -> 0번이 2번한테 1원 1번이 2번한테 1원
#
# # 매트릭스를 돌아 -> 숫자를 발견해 -> 그러면 산사람과 가격을 저장해 -> 그러면 while문 시작이야 -> 산 사람 matrix 행으로 가서 다시 팔수 있는 경우를 찾기
# # ->여기에서 경우가 있다면(기존에 그림을 사지 않았고, 지금 산 사람가격보다 크거나 같은) 그사람한테 파는거임 -> 다시 산사람 업데이트 해서 while문

import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().strip())) for _ in range(N)]

# 최대로 소유할 수 있는 사람의 수
max_count = 1  # 처음 1번 예술가 포함

# DFS 함수
def dfs(owner, visited, price):
    global max_count
    max_count = max(max_count, len(visited))  # 최댓값 갱신

    for i in range(N):
        if i not in visited and matrix[owner][i] >= price:  # 조건 만족하면 거래 가능
            dfs(i, visited | {i}, matrix[owner][i])  # 새로운 소유자로 DFS 탐색

# 1번 예술가(0번 인덱스)부터 탐색 시작
dfs(0, {0}, 0)

print(max_count)

