def solution(prices):
    answer = []
    for idx, price in enumerate(prices):
        num = 0
        if len(prices) > idx+1:
            for check in price[idx+1:]:
                if check>= price:
                    num+=1
                else:
                    answer.append(num)
                    num = 0
                    break
        else:
            answer.append(num)
    return answer
solution([1,2,3,2,3])