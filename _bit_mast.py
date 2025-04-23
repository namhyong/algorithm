# 비트를 활용한 부분집합 구하기
letters = ['a', 'b', 'c']

for i in range(1 << len(letters)):  # 총 2³, 8개의 경우의 수 체크
    selected = []
    for j in range(len(letters)): # 각각 비트를 한칸씩 옮기며 대조
        print(bin(i)
        print(bin(1<<j))
        if i & (1 << j):  # 1칸씩 왼쪽으로 옮겨가며 총 3칸을 대조해본다.
            selected.append(letters[j]) # 대조 결과가 성공이라면 selected에 append!

    print(selected)

# []                | => (i = 0) => 0 0 0 => 공집합
# ['a']             | => (i = 1) => 0 0 1 => (j = 0)에서 걸려 'a'가 뽑힘
# ['b']             | => (i = 2) => 0 1 0
# ['a', 'b']        | => (i = 3) => 0 1 1
# ['c']             | => (i = 4) => 1 0 0 => (j = 2)에서 걸려 'c'가 뽑힘
# ['a', 'c']        | => (i = 5) => 1 0 1
# ['b', 'c']        | => (i = 6) => 1 1 0
# ['a', 'b', 'c']   | => (i = 7) => 1 1 1