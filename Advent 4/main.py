sum=0
grid = []
with open("input.txt","r")as file:
    for line in file:
        grid.append(list(line.strip()))
def findHorizontal(grid):
    sum = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])-3):
            if grid[row][col] == "X" and grid[row][col+1]=="M"and grid[row][col+2]=="A"and grid[row][col+3]=="S":
                sum+=1;
            if grid[row][col] == "S" and grid[row][col+1]=="A"and grid[row][col+2]=="M"and grid[row][col+3]=="X":
                sum+=1;
    return sum;
def findVertical(grid):
    sum = 0
    for row in range(len(grid)-3):
        for col in range(len(grid[row])):
            if grid[row][col] == "X" and grid[row+1][col]=="M"and grid[row+2][col]=="A"and grid[row+3][col]=="S":
                sum+=1;
            if grid[row][col] == "S" and grid[row+1][col]=="A"and grid[row+2][col]=="M"and grid[row+3][col]=="X":
                sum+=1;
    return sum
def findRightLeaning(grid):
    sum = 0
    for row in range(len(grid)-3):
        for col in range(3,len(grid[row])):
            if grid[row][col] == "X" and grid[row+1][col-1]=="M"and grid[row+2][col-2]=="A"and grid[row+3][col-3]=="S":
                sum+=1;
            if grid[row][col] == "S" and grid[row+1][col-1]=="A"and grid[row+2][col-2]=="M"and grid[row+3][col-3]=="X":
                sum+=1;
    return sum
def findLeftLeaning(grid):
    sum = 0
    for row in range(len(grid)-3):
        for col in range(len(grid[row])-3):
            if grid[row][col] == "X" and grid[row+1][col+1]=="M"and grid[row+2][col+2]=="A"and grid[row+3][col+3]=="S":
                sum+=1;
            if grid[row][col] == "S" and grid[row+1][col+1]=="A"and grid[row+2][col+2]=="M"and grid[row+3][col+3]=="X":
                sum+=1;
    return sum


def findMas(grid):
    sum =0
    for row in range(1,len(grid)-1):
        for col in range(1,len(grid[row])-1):
            if grid[row][col]=="A":
                if(grid[row-1][col-1]=="M"and grid[row+1][col+1]=="S")or\
                (grid[row-1][col-1]=="S"and grid[row+1][col+1]=="M"):
                    if(grid[row-1][col+1]=="M"and grid[row+1][col-1]=="S")or\
                    (grid[row-1][col+1]=="S"and grid[row+1][col-1]=="M"):
                        sum+=1
    return sum







sum = findHorizontal(grid)+findVertical(grid)+findLeftLeaning(grid)+findRightLeaning(grid)

print(findMas(grid))



