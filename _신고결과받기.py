def solution(id_list, report, k):

    #:{frodo: 누가 신고했는지 배열로 }
    # 리스트의 길이 len()해서 k 보다 크면 리스트에 있는 애들 받는 리포트 횟수에 +1 해주기
    # 그러나 중복 적용 안되게 조건 절로 신고당한거 넣어줄때 in을 사용하여 있으면 안넣기
    #받는 리포트 횟수
    #:{muzi:n, frodo:n}
    reported_dict ={}
    answer_dict = {reporter:0 for reporter in id_list }
    for i in report:
        reporter, reported = i.split()
        if reported in reported_dict:
            if reporter not in reported_dict[reported]:
                reported_dict[reported].append(reporter)
        else:
            reported_dict[reported] = [reporter]
    for reporter in reported_dict.values():
        if len(reporter) >= k:
            for j in reporter:
                answer_dict[j]+=1
    return list(answer_dict.values())

print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))