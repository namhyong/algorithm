m,d = map(int,input().split())
cal = [0,31,28,31,30,31,30,31,31,30,31,30,31]
day = d
for i in range(m):
    day+=cal[i]
day%=7
check = {1:"MON",2:"TUE",3:"WED",4:"THU",5:"FRI",6:"SAT",0:"SUN"}
print(check[day])
