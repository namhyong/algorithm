def solution(survey, choices):
    # 각각 성격이 몇점인지 나타낼 리스트 딕셔너리 형태 둘중 하나로 나오기 때문에 리스트로 2개씩 나눠 놓은 모습
    chart  = [{"R":0,"T":0},{"C":0,"F":0},{"J":0,"M":0},{"A":0,"N":0}]
    # 각각의 번호가 선택 되었을때 얻는 점수
    choices_chart = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    # 정답이 들어갈 리스트
    answer = []
    # survey와 choices를 같이 루프 돌림
    for i,j in zip(survey, choices):
        # 같이 있는 문자열을 왼쪽과 오른쪽 문자로 분리
        left, right =  "".join(i)
        # 선택한 번호를 choice_chart에서 탐색하여 더할 값을 저장
        plusNum = choices_chart[j]
        # 선택된 번호가 4보다 작은 경우는 왼쪽 문자에 점수를 더해야 함
        if j<4:
            for target_chart in chart:
                # 점수를 저장할 리스트를 탐색하면서 해당 문자가 있다면 그 문자키의 값에 점수를 더해줌
                if left in target_chart:
                    target_chart[left]+=plusNum
        # 선택된 번호가 4보다 큰 경우 오른쪽 문자에 점수를 더해야 함
        elif j>4:
            for target_chart in chart:
                if right in target_chart:
                    target_chart[right]+=plusNum
        else:
            # 선택된 번호가 4인 경우는 아무일도 일어나지 않기 때문에 continue
            continue
    # 점수가 저장된 차트로 어떤 값이 선택됐는지 알아보기 위한 for루프
    for i in chart:
        # 리스트별 인덱스를 보면 2개의 키 값이 있고 둘중 더 높은 값을 가진 키가 선택되어 정답에 append 된다
        for i,(key, value) in enumerate(i.items()):
            # 인덱스와 키, 값을 뽑아내어 처음 인덱스는(0) left 두번째 인덱스는(1)은 right로 분리
            if i == 0:
                left = value
                leftKey = key
            else:
                right = value
                rightKey = key
        # left 값이 right 값 보다 크거면 left append 또는 같으면 알파벳 순서에 따라 다시 left append
        # 알파벳 순서는 애초에 chart 리스트 딕셔너리를 구성할때 알파벳 순서에 맞게 키 값 순서를 구성해서 따로 구현 X
        if left>right or left == right:
            answer.append(leftKey)
        elif left<right:
            answer.append(rightKey)

    return "".join(answer)

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))