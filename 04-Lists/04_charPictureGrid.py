grid = [['.', '.', '.', '.', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['.', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.']]

print("\nOriginal Picture grid:\n")
print(grid)

print("\nReorganized Picture grid:\n")
for y in range(0, len(grid[0])):
    rowStr = ""
    for x in range(0, len(grid)):
        rowStr += grid[x][y]
    print(rowStr)

