'''
이전에 풀었던 문제

문제 다시 읽기 9:00

많이 볼 수 있는 dp 문제

물이 잠긴 지역을 주의

n,m 순서에 주의

'''


def solution(m, n, puddles):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]  # n x m map을 만들어줌
    dp[1][1] = 1  # 집의 위치

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i == 1 and j == 1) or [j, i] in puddles:  # 웅덩이가 있는 경우 가는 루트의 경우의 수를 갱신해주지 않음
                continue
            dp[i][j] += (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    return dp[n][m]
