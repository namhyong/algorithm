# def solution(points, routes):
#     # r이 c보다 먼저 즉, y축 먼저 이동
#     # routes는 4포인트에서 2포인트로, 1포인트에서 3포인트로 2포인트에서 4포인트로 -> 3,2 -> 4,7
#     # [[0,0,0,4,0,0,0]
#     #  [0,0,0,[1,4],0,0,0]
#     #  [0,1,0,[2,3],0,0,0]
#     #  [0,[1],[2,2],[3],[4],[5],3]
#     #  [0,0,0,[4,1],0,0,0]
#     #  [0,0,0,2,0,0,0]
#     #  ]
#     # 이처럼 이동경로를 기록하고 같은 위치에 같은 숫자가 있으면 충돌로 기록
#     max_value = max(max(row) for row in points)
#     matrix = [[0 for _ in range(max_value + 1)] for _ in range(max_value + 1)]
#     for i in range(len(points)):
#         r, c = points[i]
#         matrix[r][c] = i+1
#     for i in routes:
#         start_r, start_c = points[i.pop(0) - 1]
#         while i:
#             end_r, end_c = points[i.pop(0) - 1]
#             check_r = 1
#             check_c = 1
#             if start_r > end_r :
#                 move = -1
#             else:
#                 move = 1
#             for j in range(start_r + 1, end_r,move):
#                 if matrix[j][start_c] != 0:
#                     matrix[j][start_c].append(check_r)
#                 else:
#                     matrix[j][start_c] = []
#                     matrix[j][start_c].append(check_r)
#                 check_r += 1
#                 print(matrix)
#             if start_c > end_c:
#                 move = -1
#             else:
#                 move = 1
#             for j in range(start_c + 1, end_c,move):
#                 if matrix[end_r][j] != 0:
#                     matrix[end_r][j].append(check_r)
#                 else:
#                     matrix[end_r][j] = []
#                     matrix[end_r][j].append(check_r)
#                 check_c += 1
#             start_r = end_r
#             start_c = end_c
#
#     # return matrix
# print(solution([[3, 2], [6, 4], [4, 7], [1, 4]],[[4, 2], [1, 3], [2, 4]]))

# [[0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 4, 0, 0, 0],
#  [0, 0, 0, 0, [1], 0, 0, 0],
#  [0, 0, 1, 0, [2], 0, 0, 0],
#  [0, 0, 0, 0, [3], 0, 0, 3],
#  [0, 0, 0, 0, [4], 0, 0, 0],
#  [0, 0, 0, 0, 2, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0]]

# [[0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 1, 2, 0, 0, 0, 3],
#  [0, 0, 0, 0, 0, 0, 0, [1, 1]],
#  [0, 0, 0, 0, 0, 0, 0, [2, 2]],
#  [0, 0, 5, 0, 0, 0, 0, [3, 3]],
#  [0, 0, 0, 0, 0, 0, 4, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0]]

def solution(points, routes):
    # 최대 좌표값 구하기
    max_r = max(point[0] for point in points)
    max_c = max(point[1] for point in points)

    # 매트릭스 초기화: 모든 좌표를 빈 리스트로 설정
    matrix = [[[] for _ in range(max_c + 1)] for _ in range(max_r + 1)]

    # 충돌 횟수 기록 변수
    collision_count = 0

    # 각 로봇의 경로 기록
    for robot_id, route in enumerate(routes, start=1):  # 로봇 ID는 1부터 시작
        start_r, start_c = points[route[0] - 1]
        time = 0  # 시간 초기화

        for next_point in route[1:]:
            end_r, end_c = points[next_point - 1]

            # r 좌표 이동 (r이 먼저 이동)
            step_r = 1 if end_r > start_r else -1
            for r in range(start_r, end_r, step_r):
                time += 1
                # 충돌 기록
                matrix[r][start_c].append((robot_id, time))
                if len([robot for robot, t in matrix[r][start_c] if t == time]) > 1:
                    collision_count += 1

            # c 좌표 이동 (그다음 c 이동)
            step_c = 1 if end_c > start_c else -1
            for c in range(start_c, end_c, step_c):
                time += 1
                # 충돌 기록
                matrix[end_r][c].append((robot_id, time))
                if len([robot for robot, t in matrix[end_r][c] if t == time]) > 1:
                    collision_count += 1

            # 시작점 업데이트
            start_r, start_c = end_r, end_c

    # 충돌 횟수 반환
    return collision_count
print(solution([[3, 2], [6, 4], [4, 7], [1, 4]],[[4, 2], [1, 3], [2, 4]]))