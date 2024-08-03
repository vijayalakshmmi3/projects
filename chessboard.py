def queens(board,row,n):
    if row==n:
        for i in board:
            print(i)
        print("*"*30)
        return
    for col in range(n):
        if issafe(board,row,col,n):
            board[row][col]=1
            if queens(board,row+1,n):
                print("True")
            board[row][col]=0
        
