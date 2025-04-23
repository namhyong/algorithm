#["0시:0분 차량번호, IN/OUT"]
# 누적 주차시간 구하기
# 기본요금이 있고, 기본요금 초과 주차시 기본 분당 추가요금 발생
# 출차 내역이 없다면, 23:59분에 출차로 기록
#{5961:[05:34,07:59,22:59],[]}
# 여기서 만약 arr이 홀수이면 append 23:59분
#일단 split 해서
fees = [180,5000,10,600]
records =["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
result = []
time = []
carNum = []
minute = []
InOut =[]
num = {}
for i in records:
    newRecord = i.split()
    time.append(newRecord[0])
    carNum.append(time)
print(time)
for i in time:
    newTime = i.split(":")
    minute.append(int(newTime[0])*60+int(newTime[1]))
print(minute)
for i in range(len(carNum)):
    num[carNum[i]]=[]
print(num)