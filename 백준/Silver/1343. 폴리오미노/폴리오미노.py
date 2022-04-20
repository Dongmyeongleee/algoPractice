board = input()

pa = 'AAAA'
pb = 'BB'
dot = '.'
result = ''
i = 0

while i < len(board):
    if board[i] == '.':
        result += dot
        i = i + 1
    elif board[i:i+4] == 'XXXX':
        result += pa
        i = i + 4
    elif board[i:i+2] == 'XX':
        result += pb
        i = i + 2
    else:
        break





# print(result)
if len(board) == len(result):
    print(result)
else:
    print(-1)
