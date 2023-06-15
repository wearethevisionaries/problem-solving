# 02:37 - 문제 다 읽음, 3중 for문으로 배열 하나하나 다 확인하면 정확성만 통과할 듯
#       - 그래도 어떻게 풀어야할지 아직 감은 안잡힘
# 06:32 - skill을 재구성하면 타입1, 타입2 두번에 해결가능하지 않을까
# 10:14 - 그걸 어떻게 해야할지 모르겠다. 일단 정확성만이라도 통과해보자
# 18:00 - 3중 for문으로 하니까 정확하게 정확성만 통과함 ㅋㅋㅋ...
#       - board를 펴서 생각하면 어떨까
# 30:00 - 일단 GG
# 44:40 - 생각해보니까 펴서 해도 그냥 하면 계산량은 똑같은듯

def solution(board, skill):
    cumsum = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    answer = 0
    
    for t, r1, c1, r2, c2, d in skill:
        cumsum[r1][c1] += -d if t == 1 else d
        cumsum[r1][c2 + 1] += d if t == 1 else -d
        cumsum[r2 + 1][c1] += d if t == 1 else -d
        cumsum[r2 + 1][c2 + 1] += -d if t == 1 else d
    
    for i in range(len(cumsum) - 1):
        for j in range(len(cumsum[0]) - 1):
            cumsum[i][j + 1] += cumsum[i][j]        
    for j in range(len(cumsum[0]) - 1):
        for i in range(len(cumsum) - 1):
            cumsum[i + 1][j] += cumsum[i][j] 
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += cumsum[i][j]
            if board[i][j] > 0:
                answer += 1
    
    return answer        

# def solution(board, skill):
#     answer = 0
#     for s in skill:
#         t, r1, c1, r2, c2, d = s
#         for r in range(r1, r2 + 1):
#             for c in range(c1, c2 + 1):
#                 board[r][c] += -d if t == 1 else d
#     for row in board:
#         for col in row:
#             answer += 1 if col > 0 else 0
#     return answer