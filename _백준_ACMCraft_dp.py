from collections import deque
import sys
# T = int(input())
# for _ in range(T):
#     # 건물 개수 N, 건설 순서 규칙 K
#     N,K = map(int,input().split())
#     # 건물당 걸리는 시간
#     D = list(map(int,input().split()))
#     # 건물 순서
#     XY = [list(map(int,input().split())) for _ in range(K)]
#     # 승리하기위해 건설해야하는 번호
#     W = int(input())
#     dp  = [[] for _ in range(N+1)]
#     dp[1].append(D[0])
#     for X,Y in XY:
#         # 값을 더해서 해당 위치가 빈 값이면 넣어주고
#         # 빈값이 아니라면 값을 비교해서 작은쪽을 넣기
#         if not dp[X]:
#             dp[X].append(D[X-1])
#         check = dp[X][0]+D[Y-1]
#         if not dp[Y]:
#             dp[Y].append(check)
#         else:
#             if dp[Y][0] < check:
#                 dp[Y][0] = check
#     if dp[W]:
#         print(dp[W][0])
#     else:
#         print(D[W-1])
#     print(XY)
#     print(dp)
# 처음엔 단순히 앞부터 건물을 지어가면서 기록하고 오래 걸리는 시간을 채택해서 다음 수로 넘겨주는 방법을 사용하려고 했음
# 하지만, 모든 건물이 건물 번호대로 순차적으로 지어지는 종속을 가지고 있지 않기 때문에 기각
    # [[][][][99997+99994][99994+99990]]
    # 건물 번호 순서에 대해서는 순차가 없음(지어지는 순서에 따른 관계만 있음)
    # 100000 99999 99997 99994 99990
    # 399990
                # 4->5
    #        3->     5
    #        3->  4
    #    2 ->        5
    #    2 ->     4
    #    2 ->3
    #  1->           5
    #  1->        4
    #  1 ->  3
    # 99999 99997 99994
    # 3999990

# 이후 위상정렬을 사용해 건물별 위상 즉, 해당 건물을 짓기 위해 필요한 시간들 중 가장 오래걸리는 시간을 dp에 업데이트 하는 방식으로 바꿈
# 최종적으로 이전 dp 값과 현재 건물을 짓는 시간 중 가장 큰 값이 dp로 업데이트 되는 방식
T = int(input())
res = []
for _ in range(T):
    # 건물 개수 N, 건설 순서 규칙 K
    N,K = map(int,sys.stdin.readline().split())
    # 건물당 걸리는 시간
    D = [0]+list(map(int,sys.stdin.readline().split()))
    # 건물 순서
    XY = [list(map(int,sys.stdin.readline().split())) for _ in range(K)]
    # 승리하기위해 건설해야하는 번호
    W = int(sys.stdin.readline())
    # 건물 그래프
    graph = [[] for _ in range(N+1)]
    # 건물 짓는 시간을 비교할 dp
    dp = [0]*(N+1)
    # 건물별 사전에 지어야 하는 건물이 몇개인지 나타낼 위상
    indegree = [0] * (N + 1)
    # 그래프를 그리고 Y를 짓기 위해 필요한 위상이 X이기 때문에 Y의 위상을 1증가 시킴
    for X,Y in XY:
        graph[X].append(Y)
        indegree[Y]+=1
    # 큐를 만들어 위상없이 바로 지을 수 있는 건물들을 확인
    q = deque()
    # 위상 없이 지을 수 있는 건물은 무조건 그 건물 짓는 시간이 걸리기 때문에 dp를 해당 건물 짓는 시간읋 업데이트 함
    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = D[i]
    # 위상 없이 지을수 있는 건물들이 없을때 까지 while
    while q:
        tmp = q.popleft()
        # 그래프 에서 해당 건물에서 다음 지을 수 있는 건물들을 모두 탐색 graph[tmp]
        for i in graph[tmp]:
            # 하나 탐색 할 때마다 다음 건물은 tmp건물을 지은 상황이기 때문에 위상이 하나씩 줄어들게됨
            indegree[i]-=1
            # i건물을 지을때는 위상 tmp가 필요한상황
            # tmp 지을 때 걸리는 시간 dp[tmp](이전 과정 혹은 위상이 없는 경우에는 D[i]로 기록 해왔음)
            # 과 현재 지을 건물 i를 지을 때 걸리는 시간 D[i]를 합한 dp[tmp]+D[i]가
            # 이전에 해당 건물을 지었다면 기록 됐을 dp[i]값을 비교하여 더 시간이 오래 걸리는 쪽으로 dp[i]를 업데이트
            dp[i] = max(dp[tmp]+D[i],dp[i])
            if indegree[i] == 0: # 위 과정을 통해 해당 건물의 위상이 다 없어졌다면 i건물 이후 다음 지을 건물을 확인 하기위해 q로 넣기
                q.append(i)
    res.append(dp[W])
for i in res:
    print(i)
