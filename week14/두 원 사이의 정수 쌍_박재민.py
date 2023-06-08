# 00:35 - 문제 다 읽음, 쉽지 않네
# 02:00 - 안쪽 원에 외접하는 사각형 + 바깥쪽 원에 내접하는 사각형(둘이 같을수도 있음) + 그 사이의 사각형
# 09:00 - 사각형 좌표가 8 -> 16 -> 24 -> 32순으로 8씩 증가하는걸 확인 이걸 써먹을 수 있을거 같음
# 17:21 - 안쪽 사각형 수는 맞는거같은데 바깥쪽 원의 정수좌표는 어떻게 해야할지 모르겠음(테스트만 풀림)
# 24:25 - x^2 + y^2 = r^2 식이 이거 맞나
#       - (x+y)^2 - 2xy = r^2를 만족하는 x, y 구하기
#       - 근데 이중 반복문을 안 쓰는
# 30:00 - GG, 이게 레벨 2라고?

# def solution(r1, r2):
#     r2 = 4
#     answer = 0
#     idx = r1
#     while idx != r2:
#         answer += 8 * idx
#         idx += 1
#     return answer + 4

import math


def solution(r1, r2):
    inner_dot_num = 0
    for x in range(1, r2 + 1):  # x좌표가 가질 수 있는 모든 경우의 수
        y_max = math.floor(math.sqrt(r2**2 - x**2))  # 가장 큰 정수 y좌표 구하기
        y_min = 0 if x >= r1 else math.ceil(math.sqrt(abs(r1**2 - x**2)))  # 가장 작은 정수 y좌표 구하기(이부분 아직 이해 안됨)
        inner_dot_num += y_max - y_min + 1

    return inner_dot_num * 4  # 1사분면에 대한 좌표만 계산했으니까 4번 반복
