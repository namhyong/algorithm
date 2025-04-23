# import heapq
# a = [3,2,14,13,5,56]
# heapq.heapify(a)
# print(a[3])
# while a:
#     b = heapq.heappop(a)
#     print(b)

# 통나무의 길이는 L이고, K개의 위치에서만 자를 수 있음
# 통나무를 자를수 있는 최대 횟수는 C
# 통나무의 가장 긴 조각을 작개 만들기

# 첫째줄 L,C,K
# 둘째줄 통나무를 자를 수 있는 위치
# 예를들어
# 9 2 1
# 4 5
# 이렇게 들어오면 9길이의 통나무중 2군데서 자를 수 있고 이때 위치는 4 혹은 5여야하며 이중 한 곳만 자를 수 있다.

import sys
input = sys.stdin.readline

l, k, c = map(int, input().split())
position = sorted(list(set([0, *list(map(int, input().split())), l])))
# 나무토막들
pieces = [position[i] - position[i-1] for i in range(1, len(position))]
start = 1
end = l

while start <= end:
    mid = (start + end) // 2
	# 애초에 자를 수 없으면 크기를 키움
    if max(pieces) > mid:
        start = mid + 1
    else:
        total = 0
        cnt = 0
        # 토막들의 뒤부터 확인
        for p in pieces[::-1]:
            total += p
            if total > mid:
                total = p
                cnt += 1
        if cnt > c:
            start = mid + 1
        else:
        	# 적절한 크기
            ans_result = mid
            # 최대횟수를 모두 사용하면 total,
            # 그렇지 않다면 맨 앞토막의 끝
            ans_front = total if cnt == c else pieces[0]
            end = mid - 1

print(ans_result, ans_front)