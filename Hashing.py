# id_list: 활동하는 아이디 리스트 ,
# report: 누가 누구를 신고했는지
# k: 받은 신고가 누적되어서 k를 넘으면 정지
# result: 정지 시킨 사람이 몇명인지를 나타내는 list로 id_list값 순서대로이다.
# 중복은 없어야 함
# set -> 중복 없애고
# 사람별로 신고당한 횟수를 dict로 기록
# 만약 위 dict에서 k를 넘는 사람이 있다면 for문을 돌면서 dict의 사람을 report에서 조회해서 그 전 인덱스 사람을 결과값 dict에서 +1
# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k =2
# dict_answer = dict.fromkeys(id_list,0)
# lset = list(set(report))
# new_list = []
# report_dict ={}
# overTheK = []
# answer =[]
# print(dict_answer)
# for i in lset:
#     new_list.append(i.split())
# for j in range (len(new_list)):
#     report_dict[new_list[j][1]] = report_dict.get(new_list[j][1],0)+1
# for x in report_dict:
#     if report_dict[x] >=k:
#         overTheK.append(x)
#
# for z in overTheK:
#     for y in range(len(new_list)):
#         if z == new_list[y][1]:
#             dict_answer[new_list[y][0]]=dict_answer.get(new_list[y][0])+1
# for a in dict_answer:
#     answer.append(dict_answer[a])
# print(answer)
#_____________________________시간 초과__________________________________

#set 중복제거 -> 키 벨류로 report 만들기
#신고당한 횟수를 저장하기 위한 {'muzi': 0, 'frodo': 0, 'apeach': 0, 'neo': 0} 형태 딕셔너리 만들기
# 딕셔너리 순회하면서 신고당한 사람을 찾아다니면서 해당 사람을 ++
# 이 신고당한 횟수 딕셔너리에서 값이 k 이상인 것 찾아서

