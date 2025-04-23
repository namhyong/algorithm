from itertools import combinations
def solution(number, k):
    numbers = list(map(int,"".join(number)))
    max_num = numbers.index(max(numbers[:k+1]))
    del_count = k - max_num
    number = numbers[max_num:]
    # 앞부터 돌아다니면서 뒷 갚이 앞 값보다 크면 없애기
    l,r = 0,1
    if del_count ==0:
        return "".join(list(map(str,number)))
    while del_count:
        if number[l] < number[r]:
            number.pop(l)
            del_count-=1
            continue
        else:
            l+=1
            r+=1
            if r == len(number)-1:
                break
    if del_count:
        for i in range(del_count):
            number.pop(number.index(min(number)))
    return "".join(list(map(str,number)))

print(solution("122222222434321",10))