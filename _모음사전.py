def dfs(check, n):
    global sel
    global word
    global word_list
    if sel == [1, 1, 1, 1, 1]:
        return n
    if check == "".join(word):
        return n
    for i in range(len(sel)):
        check[i] == word_list[i]
        sel[i] = 1
        n += 1
        dfs(check, n)

    return number


def solution(word):
    word_list = ["A", "E", "I", "O", "U"]
    sel = [0 * len(word_list)]
    answer = dfs(check[0 * len(word_list)], 0)
    return answer