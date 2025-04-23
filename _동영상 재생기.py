def solution(video_len, pos, op_start, op_end, commands):
    op_start_min, op_start_sec = op_start.split(":")
    op_end_min, op_end_sec = op_end.split(":")
    op_start_min = int(op_start_min)
    op_start_sec = int(op_start_sec)
    op_end_min = int(op_end_min)
    op_end_sec = int(op_end_sec)
    video_min, video_sec = video_len.split(":")
    video_min = int(video_min)
    video_sec = int(video_sec)
    def check_op(minute,second):
        if op_start_min*60+op_start_sec <=minute*60+second<=op_end_min*60+op_end_sec:
            minute = op_end_min
            second = op_end_sec
        return minute,second
    for i in commands:
        minute, second = pos.split(":")
        minute = int(minute)
        second = int(second)
        minute, second = check_op(minute,second)
        if i == "prev":
            if second >= 10:
                second-=10
            else:
                if minute == 0:
                    second = 0
                else:
                    minute-=1
                    second+=50
        else:
            if second < 50:
                second+=10
            else:
                minute+=1
                second-=50
            if video_min*60+video_sec<minute*60+second:
                minute = video_min
                second = video_sec
        minute, second = check_op(minute,second)
        pos = str(minute)+":"+str(second)
    if len(pos) != 5:
        minute, second = pos.split(":")
        if len(minute) ==1:
            minute = "0"+minute
        if len(second) ==1:
            second= "0"+second
        pos = minute+":"+second
    return pos
print(solution("30:35", "30:30", "01:00", "02:00", ["next"]))
# 반례입니다.
# 입력값 〉
# 기댓값 〉 "06:55"