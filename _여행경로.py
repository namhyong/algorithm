from collections import defaultdict, deque


def solution(tickets):
    # 티켓: a,b 는 a to b
    tickets_dict = defaultdict(list)

    for a, b in tickets:
        tickets_dict[a].append(b)
    for key in tickets_dict:
        tickets_dict[key].sort(reverse=True)
    stack = deque(["ICN"])
    visited = []
    while stack:
        current = stack.pop()
        visited.append(current)
        next_stack = tickets_dict[current]
        if next_stack:
            for i in next_stack:
                stack.append(i)
        tickets_dict[current] = []
    return visited
# defaultdict(<class 'list'>, {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['SFO', 'ICN']})
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))