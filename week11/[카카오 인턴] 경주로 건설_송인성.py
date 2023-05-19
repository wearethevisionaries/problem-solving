# 05.19 10:10~

# 직선 도로 - 100원, 코너 - 500원
# 최소 비용으로 도달해야 된다.
from collections import deque

# 일직선 100원, 코너 600원 적용 해주기 위해 방향이 90도 꺽이는 것을 판단한다.
def calc_cost(cur_dir, next_dir, cost):
    if (cur_dir == 'R' or cur_dir == 'L') and (next_dir == 'L' or next_dir == 'R'):  
        return cost + 100
    if (cur_dir == 'D' or cur_dir == 'U') and (next_dir == 'D' or next_dir == 'U'):  
        return cost + 100
    if (cur_dir == 'R' or cur_dir == 'L') and (next_dir == 'D' or next_dir == 'U'):  
        return cost + 600
    if (cur_dir == 'D' or cur_dir == 'U') and (next_dir == 'R' or next_dir == 'L'):  
        return cost + 600

    
def bfs(x, y, cost, direction):
    queue = deque([(x, y, cost, direction)])
    check = [[0 for _ in range(N)] for _ in range(N)]
    check[x][y] = 1
    while queue:
        x, y, cost, cur_dir = queue.popleft()
        if x == N-1 and y == N-1:
            answer.append(cost)
            continue
        # 이부분에서 도움을 받았다.
        for i, j, d in (0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L'), (-1, 0, 'U'):
            new_x, new_y, new_cost = x+i, y+j, calc_cost(cur_dir, d, cost)
            if new_x < 0 or new_y < 0 or new_x >= N or new_y >= N:
                continue
            # 도움 받은 부분이다.
            # 최소 비용으로 갱신해준다.
            if not new_board[new_x][new_y]:
                if not check[new_x][new_y] or check[new_x][new_y] > new_cost:
                    check[new_x][new_y] = new_cost
                    queue.append((new_x, new_y, new_cost, d))
    

def solution(board):
    global N, check, new_board, answer
    answer = []
    N = len(board)
    new_board = [board[i][:] for i in range(N)]
    bfs(0, 0, 0, 'R')
    bfs(0, 0, 0, 'D')
    return min(answer)