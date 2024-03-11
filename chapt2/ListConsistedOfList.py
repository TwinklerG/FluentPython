board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

# a wrong way!!!
# the outer list contains three same quotations to one list
weird_board = [['_'] * 3] * 3
print(weird_board)
weird_board[1][2] = 'O'
print(weird_board)
# the same to the one below
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)
print(board)
row[1] = 'O'
print(board)
# the right version
board = []
for i in range(3):
    row = ["_"] * 3
    board.append(row)
print(board)
board[1][2] = 'O'
print(board)

t = (1, 2, [30, 40])
# not allow t[2] += [50, 60]
t[2].extend([50, 60])
print(t)
