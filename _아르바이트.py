# def solution(part_times):
#     # 1. 아르바이트를 종료 날짜 기준으로 정렬
#     part_times.sort(key=lambda x: x[1])
#
#     # 2. 종료 날짜 기준으로 dp 배열 준비
#     n = len(part_times)
#     dp = [0] * n  # dp[i]는 i번째 아르바이트까지 고려한 최대 수익
#
#     # 3. 첫 번째 아르바이트의 수익으로 초기화
#     dp[0] = part_times[0][2]
#
#     # 4. 각 아르바이트에 대해 최적의 수익 계산
#     for i in range(1, n):
#         # 현재 아르바이트 선택
#         profit = part_times[i][2]
#
#         # 현재 아르바이트와 겹치지 않는 가장 가까운 아르바이트 찾기
#         # print(part_times)
#         for j in range(i - 1, -1, -1):
#             print(part_times[j],part_times[i])
#             if part_times[j][1] < part_times[i][0]:
#                 profit += dp[j]
#                 break
#
#         # 이전까지의 최대 수익과 현재 선택한 수익을 비교
#         dp[i] = max(dp[i - 1], profit)
#
#     # dp 테이블의 최댓값이 최종 결과
#     return dp
# print(solution([[3,6,3],[2,4,2],[10,12,8],[11,15,5],[1,8,10],[12,13,1]]))
def solutions(part_times):
    part_times.sort(key = lambda x:x[1])
    dp = [0] * len(part_times)
    dp[0] = part_times[0][2]

    for i in range(1,len(part_times)):
        sal = part_times[i][2]
        for j in range(i-1,-1,-1):
            if part_times[j][1] <= part_times[i][0]:
                sal+=dp[j]
                break
        dp[i] = max(dp[i-1],sal)
    return dp[-1]

print(solutions([[3,6,3],[2,4,2],[10,12,8],[11,15,5],[1,8,10],[12,13,1]]))
print(solutions([[1,2,1],[1,2,2],[2,3,1],[3,4,1],[1,4,2]]))