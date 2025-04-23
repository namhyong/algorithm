import heapq as hq

def solution(n, costs):
    answer = 0
    from_to = list(list() for _ in range(n))
    visited = [False] * n
    priority = []

    for a, b, cost in costs:
        from_to[a].append((b, cost))
        from_to[b].append((a, cost))
    print(from_to)
    hq.heappush(priority, (0, 0))
    while False in visited:
        cost, start = hq.heappop(priority)
        if visited[start]: continue
        print(start)
        visited[start] = True
        answer += cost
        for end, cost in from_to[start]:
            if visited[end] : continue
            else:
                hq.heappush(priority, (cost, end))
        print(priority)
        print(visited)

    return answer
print(solution(4,[[0,1,1],[1,3,1],[0,2,2],[1,2,5],[2,3,8]]))