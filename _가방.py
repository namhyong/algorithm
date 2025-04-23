def solutions(bag, capacity):
    bag.sort(key = lambda  x: x[0])
    # print(bag)
    dp = [[0,0] for _ in range(len(bag))]
    print(dp)
    dp[0][0] = bag[0][0]
    dp[0][1] = bag[0][1]

    for i in range(1, len(bag)):
        weight, val = bag[i][0], bag[i][1]
        for j in range(i-1,-1,-1):
            print(dp[j][0])
            if dp[j][0]+weight <= capacity:
                val+=dp[j][1]
                weight+=dp[j][0]
                break
        if dp[i-1][1] > val:
            dp[i][0], dp[i][1] = dp[i-1][0], dp[i-1][1]
        else:
            dp[i][0], dp[i][1] = weight, val
    print(dp)
    return dp[-1][1]
print(solutions([[2,3], [3,4],[4,5], [5,6]],7))