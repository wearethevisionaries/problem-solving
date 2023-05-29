# 05.29 11:20 ~ 13:00
# 공부하면서 플었다.
# 10억 이상의 수로 나눈 나머지 -> DP 문제이다.
# [[2,2]] 의 위치를 보았을 때 집의 위치 [[1,1]] 이다.
# 좌표가 일반적인경우와 반대로 되어있다.

def solution(m, n, puddles):
    # 좌표 (m,n)이 일반적인 (n,m)에 맞게 설정한다. (1,1) 부터 시작하므로 1씩 더해서 설정해준다.
    dp = [[0] * (m+1) for i in range(n+1)]
    # puddles 좌표를 바꿔야 된다.
    puddles = [[p, q] for [q, p] in puddles]
    # 집의 위치 표시한다.
    dp[1][1] = 1
    
    # n행 부터 읽어간다.
    for i in range(n+1):
        # m열을 읽는다.
        for j in range(m+1):
            if i==1 and j==1: continue
            # puddle 포함되면 0 값을 취한다.
            if [i, j] in puddles:
                dp[i][j] = 0
            # 왼쪽, 위의 합으로 표현된다.
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    return dp[n][m]