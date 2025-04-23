from collections import Counter
def solution(citations):
    citations.sort(reverse = True)
    max_citations = citations[0]
    citations = dict(Counter(citations))
    count = 0
    for i in range(max_citations,-1,-1):
        if citations[i]:
            count += citations[i]
        if count >= i:
            break
    return count
solution([3, 0, 6, 1, 5])