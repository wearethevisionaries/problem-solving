'''
문제 읽기 9:30

모든 경우의 수 탐색

combinations_with_replacement가 있다.

bfs로도 풀 수 있다.

완료 10:30
'''

from itertools import combinations_with_replacement


def solution(n, info):

    answer = [-1]
    gap = -1

    for score_list in list(combinations_with_replacement(range(11), n)):
        lion_score = 0
        apeach_score = 0

        score_board = [0 for _ in range(11)]

        for score in score_list:
            score_board[10 - score] += 1

        for i in range(11):
            if score_board[i] == 0 and info[i] == 0:
                continue
            if score_board[i] > info[i]:
                lion_score += (10 - i)
            else:
                apeach_score += (10 - i)

        if lion_score > apeach_score:
            score_gap = lion_score - apeach_score

            if score_gap > gap:
                gap = score_gap
                answer = score_board

    return answer
