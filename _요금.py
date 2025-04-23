T, K1, P1, K2, P2 = map(int,input().split())
def min_cost(T, P1, K1, P2, K2):
    INF = float('inf')
    min_cost = INF

    # 문자팩 1과 2의 구매 횟수 탐색
    max_a = (T // K1) + 1  # 문자팩 1의 최대 구매 횟수
    max_b = (T // K2) + 1  # 문자팩 2의 최대 구매 횟수

    for a in range(max_a + 1):
        for b in range(max_b + 1):
            # 문자팩으로 제공되는 총 문자 수
            total_messages = a * K1 + b * K2

            # 초과 문자 메시지 수
            extra_messages = max(0, T - total_messages)

            # 총 비용 계산
            cost = a * P1 + b * P2 + extra_messages * 10

            # 최소 비용 갱신
            min_cost = min(min_cost, cost)

    return min_cost



# 최소 비용 계산
result = min_cost(T, P1, K1, P2, K2)
print(result)
