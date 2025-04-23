def solution(input_string):
    answer =''
    count = {}
    answer_list = []
    for idx, char in enumerate(input_string):
        if char not in count:
            count[char] = [idx]
        else:
            count[char].append(idx)

    for key, value in count.items():
        if len(value)>= 2:
            for i in range(len(value)-1):
                if value[i+1]- value[i] >1:
                    answer_list.append(key)
                    break
    if len(answer_list) == 0:
        answer = "N"
    else:
        answer = ''.join(sorted(answer_list))
    return answer
print(solution(input()))

# input_string = "edeaaabbccd"
# count ={}
# answer =''
# answer_list= []
# for i in range(len(input_string)-1):
#     if input_string[i] == input_string[i+1]:
#         continue
#     else:
#         count[input_string[i]] = count.get(input_string[i],0)+1
#         if i == len(input_string)-2:
#             count[input_string[i+1]] = count.get(input_string[i+1], 0) + 1
#
# for key, value in count.items():
#     if value>=2:
#         answer_list.append(key)
# if len(answer_list) == 0:
#     answer = "N"
# else:
#     answer = ''.join(sorted(answer_list))
