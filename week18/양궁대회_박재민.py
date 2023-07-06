# 01:00 - 라이언은 어피치를 가장 큰 점수차로 이겨야 함
# 04:00 - 줄건 주는 규칙을 찾자
#       - 몇개 없는데 시간제한이 10초인거 보면 완전탐색일지도
#       - 1. 큰 점수를 어피치가 못맞췄으면 무조건 맞추는게 좋음
#       - 이거 말고는 규칙이 딱히 보이는게 없음 일단 완전탐색 ㄱㄱ

from itertools import combinations_with_replacement as com_rep


def solution(n, info):
    answer = []
    max_score_diff = 0

    for scores in com_rep(range(11), n):
        lion_score = [sum([1 for score in scores if (10 - score) == i]) for i in range(11)]

        lion, apeach = 0, 0
        for i in range(11):
            lion_sum, apeach_sum = lion_score[i], info[i]
            if lion_sum == apeach_sum == 0:
                continue
            if lion_sum > apeach_sum:
                lion += 10 - i
            else:
                apeach += 10 - i

        if max_score_diff < lion - apeach:
            max_score_diff = lion - apeach
            answer = lion_score

    return [-1] if not answer else answer
