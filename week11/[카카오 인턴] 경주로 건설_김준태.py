'''
문제 읽기 9:00

(0,0) 출발 (N-1,N-1) 도착

상하좌우로 이동 가능

최소 비용 구하기 -> DP or BFS 로 가능하지 않을까?

배열 크기 3 ~ 25

코너를 잘 구하면 되겠다.
코너인지 아닌지 어떻게 판별할까..? -> 이전에 진행되던 방향을 고려해야한다.. 9:35
1 행에는 코너가 없다.

DP로는 코너 계산이 어려울 것 같다 BFS로 하자 9:25

25번이 틀려요.. -> 질문 참고 -> BFS 2번으로 변경  9: 55

완료 10:10

후기 : 코너 계산이 까다로웠다.. 이런 bfs는 처음이다.
'''

from collections import deque


def bfs(board, d):
    n = len(board)
    price = [[600 * 25 * 25] * n for _ in range(n)]  # 최대값으로 배열 초기화
    price[0][0] = 0  # 시작 지점은 항상 0

    queue = deque()
    queue.append((0, 0, 0, d))  # (x, y, cost, dir)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y, c, d = queue.popleft()  # (x, y, cost, dir)

        for i in range(4):
            nx = x + dx[i]  # 갱신된 x 좌표
            ny = y + dy[i]  # 갱신된 y 좌표
            nd = i  # 진행 방향

            if -1 < nx < n and -1 < ny < n and board[nx][ny] != 1:  # 범위 내 좌표값 & 벽이 아닌 경우
                if nd == d:  # 방향이 이전과 같다면 직진
                    nc = c + 100
                else:  # 방향이 이전과 같지 않다면 코너
                    nc = c + 600

                if nc < price[nx][ny]:  # 최소값 갱신
                    price[nx][ny] = nc
                    queue.append((nx, ny, nc, i))

    return price[-1][-1]


def solution(board):
    answer = min(bfs(board, 0), bfs(board, 2))
    return answer
