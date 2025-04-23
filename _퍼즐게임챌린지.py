def solution(diffs, times, limit):
    max_diff = max(diffs)
    min_diff = min(diffs)
    max_num = 0
    while True:
        diff = (max_diff + min_diff) // 2
        check = 0
        for i in range(len(diffs)):
            if diffs[i] <= diff:
                check+=times[i]
            else:
                retry = diffs[i]-diff
                check+=(times[i-1]+times[i])*retry+times[i]
        if limit == check:
            answer = diff
            break
        elif limit > check:
            max_diff = diff
        else:
            min_diff = diff
        if max_diff-min_diff ==1:
            min_check = 0
            for i in range(len(diffs)):
                if diffs[i] <= min_diff:
                    min_check += times[i]
                else:
                    retry = diffs[i] - min_diff
                    min_check += (times[i - 1] + times[i]) * retry + times[i]
            if min_check > check and min_check <= limit:
                answer = min_diff
            else:
                answer = max_diff
            break
    return answer
print(solution( [1, 1, 3], [1, 1, 3], 50))