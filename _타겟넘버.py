
def solution(numbers, target):
    answer = 0
    def dfs(num,depth):
        nonlocal answer
        if depth== len(numbers):
            if num == target:
                answer+=1
            return
        signs = [num,-num]
        if depth == 1:
            for i in range(2):
                #첫 재귀 시작
                dfs(signs[i]+numbers[depth],depth+1)
                dfs(signs[i] - numbers[depth], depth + 1)
        else:
            #두번째 재귀 시작 numbers크기만큼 진행되다가 재귀 빠져나옴
            dfs(num+numbers[depth],depth+1)
            #아래 예제로 5번 재귀후 4번째 재귀로 빠져나와서 바로 -1하는 재귀 시작해서
            # 1,1,1,1,-1이되어 다시5개가 됐기 때문에 재귀 빠져나옴
            #다음으로는 1111재귀가 끝나서 111이되고 111-1재귀 시작, 111-1+1,111-1-1하고 재귀 빠져나오기 반본
            dfs(num-numbers[depth],depth+1)


    dfs(numbers[0],1)
    return answer
print(solution([1, 1, 1, 1, 1],3))