import heapq
import sys
input = sys.stdin.readline

inputN = int(input())
hq = []  # 반복문 밖에서 힙 리스트 초기화
for _ in range(inputN):
    n = int(input())
    if n == 0:
        if not hq:  # 힙이 비어 있으면 0 출력
            print(0)
        else:  # 힙에서 최소값을 꺼내서 출력
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, n)  # 힙에 값 추가
