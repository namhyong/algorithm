#2 ~ 10
# 2 -> 소인수 2 => 소수 개수 1, 1은 소수 X 틀림
# 3 -> 소인수 3 => 소수 개수 1, 1은 소수 X 틀림
# 4 -> 소인수 2*2=> 소수 개수 2 , 2는 소수 O 맞음 underPrime 1
# 5 -> 소인수 5 => 소수 개수 1 , 1은 소수 X 틀림
# 6 -> 소인수 2*3 => 소수 개수 2 , 2은 소수 O 맞음 underPrime 2
# 7 -> 소인수 7 => 소수 개수 1 , 1은 소수 X 틀림
# 8 -> 소인수 2*2*2 => 소수 개수 3 3은 소수 O 맞음 underPrime 3
# 9 -> 소인수 3*3 => 소수 개수2 2는 소수 O 맞음 underPrime 4
#10 -> 소인수 2*5 => 소수 개수 2 2는 소수 O 맞음  underPrime 5

a , b = map(int, input().split())
cnt=0
for i in range(a,b+1):
    prime = 0;
    checkPrime = 0
    if i>=2:
        for j in range(2,i+1):
            if i%j !=0:
                continue
            elif i%j ==0:
                 i=i/j
                 prime+=1
                 break
    if prime ==1:
        continue
    else:
        for k in range(2,prime+1):
            if prime%k==0:
                break
            else:
                checkPrime+=1
        if checkPrime == prime-2:
            cnt+=1
print(cnt)


