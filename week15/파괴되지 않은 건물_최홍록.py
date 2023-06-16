def solution(board, skill):
    answer = 0
    temp = [[0 for i in range(len(board[0])+1)] for j in range(len(board)+1)]
    for item in skill:
        r1 = item[1]; c1 = item[2]; r2 = item[3]; c2 = item[4]; degree = item[5]

        if item[0] == 1:
            temp[r1][c1] -= degree
            temp[r1][c2+1] += degree
            temp[r2+1][c1] += degree
            temp[r2+1][c2+1] -= degree
        elif item[0] == 2:
            temp[r1][c1] += degree
            temp[r1][c2+1] -= degree
            temp[r2+1][c1] -= degree
            temp[r2+1][c2+1] += degree

    for i in range(len(temp)):
        for j in range(1,len(temp[0])):
            temp[i][j] += temp[i][j-1]
    
    for i in range(1,len(temp)):
        for j in range(len(temp[0])):
            temp[i][j] += temp[i-1][j]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += temp[i][j]

    for row in board:
        for column in row:
            if column >=1:
                answer+=1
                                                            
    return answer