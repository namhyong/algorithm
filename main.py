# my_string = "people"
# str = []
# a = set(my_string)
# for i in my_string:
#     if i in a:
#         str+= i
#         a.discard(i)
# answer = "".join(str)


# s ="hello"
# l = list(s)
# answer =[]
# dict = {}
# for i in l:
#     dict[i] = dict.get(i,0)+1
# for j in dict:
#     if dict[j] == 1:
#         answer.append(j)
# answer.sort()
# answer = "".join(answer)

# dict_num = {"zero":0, "one":1, "two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
# s = "one4seveneight"
# answer = s
# for i in dict_num:
#     answer= answer.replace(i,str(dict_num[i]))
# print(answer)
# for i in range(len(l)):
#     if l[i]=="z":
#         answer.append(0)
#         i+=4
#     elif l[i]=="o":
#         answer.append(1)
#         i+=3
#     elif l[i]=="t":
#         i+=1
#         if l[i]=="w":
#             answer.append(2)
#             i+=2
#         elif l[i]=="h":
#             answer.append(3)
#             i+=4
#     elif l[i]=="f":
#         i+=1
#         if l[i]=="o":
#             answer.append(4)
#             i+=3
#         elif l[i]=="i":
#             answer.append(5)
#             i+=3
#     elif l[i]=="s":
#         i+=1
#         if l[i]=="i":
#             answer.append(6)
#             i+=2
#         elif l[i+1]=="e":
#             answer.append(7)
#             i+=4
#     elif l[i]=="e":
#         answer.append(8)
#         i+=5
#     elif l[i]=="n":
#         answer.append(9)
#         i+=4
#     else:
#         answer.append(i)
#         i+=1
# print(answer)

id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
dict_report ={}
answer = []
new_arr = []
answer_dict = {}
set_list = list(set(report))
for i in range (len(set_list)):
    new_arr.append(set_list[i].split())
for j in range(len(new_arr)):
        dict_report[new_arr[j][1]] = dict_report.get(new_arr[j][1],0)+1
for z in id_list:
    if z in dict_report and dict_report[z] >= k:
        for x in range(len(new_arr)):
            if new_arr[x][1] == z:
                answer_dict[new_arr[x][0]] = answer_dict.get(new_arr[x][0],0)+1

for y in id_list:
    answer.append(answer_dict.get(y,0))

