board = [None for _ in range(3) for _ in range(4)]
print(board)

board=[]
for i in range(3):
    list_1=[]
    for j in range(4):
        list_1.append(None)
    board.append(list_1)
print(board)

b = [(i,j) for i in range(2) for j in range(5)]
print(b)

a = []

for i in range(2):
    for j in range(5):
        a.append((i,j))
print(a)