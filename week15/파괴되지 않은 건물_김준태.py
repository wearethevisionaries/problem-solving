'''
문제 읽기 9:00

효율성 테스트 점수가 있다.

우선 하라는 대로 스킬을 다 찍어보자.

정확성은 다 맞췄지만 효율성을 틀림 10:35

dp로 풀 수 있나?? 딱히 룰이 없어서 힘들듯
누적 합 알고리즘이 있었는데 사용해보자.

문제 완료 10:15
'''


def solution(board, skill):
    answer = 0
    M, N = len(board), len(board[0])
    maps = [[0] * (N + 1) for _ in range(M + 1)]
    
    # 모든 스킬의 영향 계산
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            damage = -degree
        else:
            damage = degree

        maps[r1][c1] += damage
        maps[r1][c2 + 1] -= damage
        maps[r2 + 1][c1] -= damage
        maps[r2 + 1][c2 + 1] += damage

    # 누적합 계산
    for i in range(N):
        for j in range(1, M):
            maps[j][i] += maps[j - 1][i]

    for i in range(M):
        for j in range(1, N):
            maps[i][j] += maps[i][j - 1]

    # 남은 건물 계산
    for j in range(M):
        for i in range(N):
            board[j][i] += maps[j][i]
            if board[j][i] > 0:
                answer += 1

    return answer
