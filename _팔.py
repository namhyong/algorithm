l, r = map(str, input().split())
cnt = 0
if len(l) != len(r):
    print(0)
else:
    for i in range(len(l)):
        if l[i] == r[i]:
            if l[i] == "8":
                cnt+=1
        else:
            break
    print(cnt)
# l = str(l)
# r = str(r)
# if len(l) == len(r):
#     if int(l) == int(r):
#         for i in range(len(r)):
#             if l[i] == "8":
#                 cnt+=1
#     else:
#         for i in range(len(r)):
#             if l[i] == "8" and r[i] == "8":
#                 cnt += 1
#             else:
#                 break
# else:
#     print(0)
# if cnt != 0:
#     print(cnt)
