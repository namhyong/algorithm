n , m = map(int,input().split())
numList =[]
answerList = []
min = 1000000001
max = 0
for _ in range(n):
    numList.append(int(input()))
abList = [list(map(int,input().split())) for _ in range(m)]

for a,b in abList:
    # targetList = numList[a-1:b]
    # targetList.sort()
    # answerList.append([targetList[0], targetList[len(targetList)-1]])
    for i in range(a-1,b):
        if numList[i]<min:
            min = numList[i]
        if numList[i]>max:
            max = numList[i]
    answerList.append([min,max])
    min = 1000000001
    max = 0
for min, max in answerList:
    print(min, max)
