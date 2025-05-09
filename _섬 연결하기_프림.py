# SWEA 5249 최소신장트리 풀이



def solution(n,costs):
    def Prim():
        dist = [987654321] * (n + 1)
        dist[n] = 0
        visited = [False] * (n + 1)

        for _ in range(n + 1):
            min_idx = -1
            min_value = 987654321

            for i in range(n + 1):  # 일단 현재 dist 배열에서 visited 안된애들 중 가장 노드 찾는 로직
                if not visited[i] and dist[i] < min_value:
                    min_idx = i
                    min_value = dist[i]  # 갱신!

            visited[min_idx] = True  # 가장 작은애로 이동할거니까 visited 넣어주고
            # 요거 주석 풀어서 visted, dist 찍어볼것!
            # print(visited, dist)

            # 이제 그 선택된 점에서부터 갈 수 있되, 더 짧은 거리를 보장한다면 dist 배열 갱신
            for i in range(n + 1):
                if not visited[i] and adj[min_idx][i] < dist[i]:
                    dist[i] = adj[min_idx][i]

        return sum(dist)  # 마지막에 dist 배열의 총합산이 MST를 이루는 간선들의 합
    adj = [[987654321] * (n+1) for _ in range(n+1)]  # inf 개념으로 큰 수 넣어줌

    for st,ed,w in costs:  # 인접행렬 만들기
        adj[st][ed] = adj[ed][st] = w  # 노드들간의 가중치 자체를 인접 행렬에 넣어서 구조화

    print(Prim(n,adj))