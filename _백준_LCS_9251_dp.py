# LCS: 최장공통부분수열
# 모두의 부분수열 중 가장 긴 것 찾기
import sys
# sys.setrecursionlimit(10 ** 8)
# a = list("".join(sys.stdin.readline().rstrip()))
# b = list("".join(sys.stdin.readline().rstrip()))
# print(a,b)
# def dfs(a,b,check):
#     for i in range(len(a)):
#         for j in range(len(b)):
#             if a[i] == b[j]:
#                 dfs(a[i:],b[j:],check+1)
#     return check
# # A
# # C A -> dfs(CATKP,PCAK)
# # C
# # P C -> ATKP,AK
# # A
# # A -> TKP,K
# # T
# # K
# # K
# # K
# print(dfs(a, b, 0))

# a를 특정 글자로 시작할 때 확인 해야함
# AC ACA, ACAY,ACAKP,ACAP
# AA
# CAY,CAKP,CAP
# AY,AK,AP
# Y
# K
# P
# 첫 글자 확인하고 다음글자넣기
s1 = list(input())
s2 = list(input())
lcs = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
print(max(map(max,lcs)))
# AC -> max(0,0)
# AA -> 0+1(이전까지의 공통 수열 부분을 찾아놓은 것에서 +1)
# AP -> else문에 걸려서 기존에 찾은 문자열 lcs와 지금열에서 찾은 문자열 중 더 큰것을 채택
# AC -> 같음
# AA -> 이전까지 찾아온 공통수열에 +1
