def solution(priorities, location):
    indexList = [1* i for i in range(len(priorities))]
    count = 0
    while priorities:
        nowProcess = priorities.pop(0)
        nowIndex = indexList.pop(0)
        if not priorities:
            count+=1
            break
        if nowProcess < max(priorities):
            priorities.append(nowProcess)
            indexList.append(nowIndex)
        else:
            count+=1
            if nowIndex==location:
                break
    return count

print(solution( [5, 4, 3, 2, 1],4))