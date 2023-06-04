'''
문제 읽기 3:00

두 원 사이공간에 x,y가 정수인 경우? -> 원 위의 좌표도 포함

수학 문제인가..?

반지름은 정수로 주어진다.

흠.. 점이 원의 넓이 안에 있으면 되겠다. 3:15
(x - a)^2 + (y - b)^2 < r^2

엣지 케이스 해결을 해야한다. (점이 정수일 때)

시간이 좀 오래걸린다. 어떻게 줄여야 할지는 모르겠다.

문제 풀이 3:55
'''

import math


def solution(r1, r2):
    answer = 0
    for x in range(1, r2 + 1):
        r1_point = 0  # r1의 원 교점
        if x <= r1:
            r1_point = math.ceil((r1 ** 2 - x ** 2) ** 0.5)  # x 범위가 r1을 벗어나면 교점이 없다.
        r2_point = math.floor((r2 ** 2 - x ** 2) ** 0.5)  # r2의 원 교점
        answer += (r2_point - r1_point + 1)  # 두 원 사이의 정수 좌표 구하기
    return answer * 4