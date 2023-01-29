def eval_w(board):
    possible = [input()]

#rows
    for i in range(3):
        possible.append( board[i][0] + board[i][1] + board[i][2] )

#columns
    for i in range(3):
        possible.append( board[0][i] + board[1][i] + board[2][i] )

#diagonals
    possible.append( board[0][0] + board[1][1] + board[2][2] )
    possible.append( board[0][2] + board[1][1] + board[2][0] )

    if 3 in possible:
        ended = True
        return 1
    elif -3 in possible:
        ended = True
        return -1
    else:
        return 0
print(eval_w())