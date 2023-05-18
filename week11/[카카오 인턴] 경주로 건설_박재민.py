# 0분 - 시작
# 1분 - 문제 다 읽음
#       당연히 최단경로 문제라고 생각했는데 #4를 보면 맞나 싶다
# 3분 - 이거 DP인가? (2차원 DP 느낌이랑 비슷한듯)
#       그런데 2차원 DP 푸는법이 기억이 안남
# 16분 - 아무리 생각해도 DP로 푸는방법 모르겠음 그냥 최단경로로 풀어보자
#       가중치가 필요할듯
# 50분 - 뭔가 제대로 안도는거같음 왜 안돌지?
# 60분 - GG
# 66분 - cost array를 만드는 부분에서 오류가 있었다...
#       참고자료: http://bitly.ws/ELYf

from collections import deque
from sys import maxsize


def BFS(board, direction):
    dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, 0, 0, direction)])
    out = len(board)
    cost = [[maxsize] * out for _ in range(out)]

    while queue:
        cx, cy, cc, cd = queue.popleft()
        for nd, (dx, dy) in enumerate(dxdy):
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < out and 0 <= ny < out and board[nx][ny] != 1:
                nc = cc + (100 if nd == cd else 600)
                if cost[nx][ny] > nc:
                    cost[nx][ny] = nc
                    queue.append((nx, ny, nc, nd))

    return cost[-1][-1]


def solution(board):
    return min(BFS(board, 0), BFS(board, 1))
