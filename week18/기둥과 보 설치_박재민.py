# 04:21 - 문제는 다 읽었는데 아직은 잘 이해가 안되는 상황
# 11:32 - 아예 공중에 떠있지만 않으면 보 설치는 상관없고 삭제가 문제일듯
#       - 일단 하고 문제가 있으면 되돌리자
# 19:29 - 빠르게 해야하나 했는데 1000개 이하라서 O(n^2)으로 풀어도 되나보다
# 20:00 - 끝


def check(answer):
    for x, y, a in answer:
        if a == 0:
            condition1 = [x - 1, y, 1] in answer
            condition2 = [x, y, 1] in answer
            condition3 = [x, y - 1, 0] in answer
            if y == 0 or condition1 or condition2 or condition3:
                continue
            return False
        elif a == 1:
            condition1 = [x, y - 1, 0] in answer
            condition2 = [x + 1, y - 1, 0] in answer
            condition3 = [x - 1, y, 1] in answer and [x + 1, y, 1] in answer
            if condition1 or condition2 or condition3:
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 1:
            answer.append([x, y, a])
            if not check(answer):
                answer.pop()
        elif b == 0:
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])
    answer = sorted(answer)
    return answer
