'''
문제 읽기 9:00

기둥과 보를 설치하면서 조건에 맞는지 확인

완료 10:20
'''


def is_possible(answer):
    for x, y, kind in answer:
        if kind == 0:  # 기둥
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        else:  # 보
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, kind, order = build

        if order == 1:
            answer.append([x, y, kind])
            if not is_possible(answer):
                answer.remove([x, y, kind])
        else:
            answer.remove([x, y, kind])
            if not is_possible(answer):
                answer.append([x, y, kind])
    answer.sort()

    return answer
