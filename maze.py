#Execute the app.py file to get the output
def relation(i,j):
    vert = 10
    vert_rem = 9

    if i == j:
        return 0
    if i % vert != 0 and i % vert != vert_rem:
            if i-1 == j or i+1 == j or i-vert == j or i+vert == j:
                return 1
            else:
                return 0
    elif i % vert == 0:
        if i+1 == j or i-vert == j or i+vert == j:
            return 1
        else:
            return 0
    elif i % vert == vert_rem:
        if i-1 == j or i-vert == j or i+vert == j:
              return 1
        else:
            return 0

m = 10
size = m*m
maze = [[0 for i in range(size)] for j in range(size)]

for i in range(0, size):
    for j in range(0, size):
        maze[i][j] = relation(i, j)
        
def return_maze():
    return maze, size