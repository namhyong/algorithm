def solution(n, costs):
    answer = 0
    uni = [0] * (n + 1)
    costs.sort(key = lambda x: x[2])
    for i in range(1,n + 1):
        uni[i] = i
    print(uni)
    # uni [0,1,2,3,4]로 초기화
    # 각 노드의 부모를 나타냄

    # 서로 다른 두 노드를 하나의 부모로 엮는 union
    def union(x,y):
        a = find(x)
        b = find(y)
        if a != b:
            uni[a] = b
    # 부모를 찾는 함수
    def find(x):
        if uni[x] == x:
            return x
        else:
            uni[x] = find(uni[x])
            return uni[x]
    for n1,n2,cost in costs:
        if find(n1) != find(n2):
            union(n1,n2)
            answer += cost
        print(uni)
    return answer
solution(4,[[0,1,1],[1,3,1],[0,2,2],[1,2,5],[2,3,8]])
# 가중치 순으로 정렬
# [[0,1,1],[1,3,1],[0,2,2],[1,2,5],[2,3,8]]
# uni = [0,1,2,3,4]
# 1번 for문:
# find(0), find(1) 실행 uni[0] == 0 return 0에 걸려 0 uni[1] == 1에 걸려 1 return
# 다음 if문에 0,1 같지 않음에 걸려 union 연산 -> 각가 0,1을 리턴하고 이들이 같지 않기 때문에 uni[0] = 1이 되어 [1,1,2,3,4]가 됨

# 2번 for문
# find(1), find(3) -> uni[1] ==1, uni[3] == 3 -> 각각 1,3 return
# 둘이 같지 않기 때문에 union하여 [1,3,2,3,4]

# 3번 for문
# find(0), find(2) -> uni[0] !=0(1임) 따라서 else문에 걸려서 uni[0] = find(uni[0]) -> find(1) (재귀1)
# find(1) -> uni[1] != 1(3임) 따라서 else문에 걸려서 uni[1] = find(uni[1]) -> find(3) (재귀2)
# find(3) -> uni[3] == 3 따라서 return 3 -> 재귀2의 return 값이 3 이기 때문에 uni[1] = 3되고 return uni[x] 실행되어 3 return
# 재귀 1의 return 값이 3이고 uni[0] = 3이 되고 3 return 되어 재귀 끝
# 현재까지 uni = [3,3,2,3,4]
# find(2) -> uni[2] ==2이기 때문에 2 return -> find(0),find(2)가 3,2로 같지 않기 때문에 union 실행
# union 실행시 find(0) ->3 , find(2) ->2 uni[3] =2로 uni = [3,3,2,2,4]

# 4번 for문
# find(1), find(2) 부모가 같은지 확인
# uni[1] != 1 -> uni[1] = find(3) ---> uni[3] != 3 -> uni[3] = find(2) ---> uni[2] = 2 return 2 따라서 uni = [3,2,2,2,4]가 되고
# uni[1] 은 2를 return
# find(2) -> uni[2] ==2  return 2
# find(1), find(2)모두 2를 리턴해서 다음 스탭

# 5번 for문
# find(2), find(3) 부모가 같은지 확인
# uni[2] = 2, uni[3] !=3 --> uni[3] = find(2) ---> uni[2] = 2 return 2 -> uni[3] = 2 -> 결국 return 2 uni는 [3,2,2,2,4]
# find(2),find(3)모두 2를 return 했기 때문에 for문 끝나고 union을 실행한 간선들의 cost만 비용합산