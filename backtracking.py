def perm(depth,num):
    if depth == N:
        new_num = sum(sel)
        if new_num < num:
            num = new_num
        return num

    for j in range(N):
        if not check[j]:
            if sum(sel)+arr[depth][j] > num:
                continue
            check[j] = 1
            sel[depth] = arr[depth][j]
            perm(depth+1, num)
            num = perm(depth+1, num)
            check[j] = 0
    return num
for tc in range(1, int(input())+1 ):
    N = int(input())
    sel = [0 for _ in range(N)]
    check = [0 for _ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    num = N*9
    perm(0,num)
    print(f'#{tc} {perm(0,num)}')
# depth:0 j:0, sel[0] = [2,0,0] ->  depth:1 j:1 sel[1] = [2,8,0] -> depth:2 j:2, sel[2] =[2,8,2]
# j:


# 2 8 2
# 2 5 2
# 1 5 2 o
# 1 5 7
# 2 5 2
# 2 8 7


# def perm(depth):
#     if depth == N:
#         new_num = sum(sel)
#         answer.append(new_num)
#         return
#     for j in range(N):
#         if not check[j]:
#             check[j] = 1
#             sel[depth] = arr[depth][j]
#             perm(depth+1)
#             check[j] = 0
# for tc in range(1, int(input())+1 ):
#     N = int(input())
#     sel = [0 for _ in range(N)]
#     check = [0 for _ in range(N)]
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     answer = []
#     perm(0)
#     print(f'#{tc} {min(answer)}')