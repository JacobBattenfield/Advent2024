import copy
#Define an empty map

map = []
#Fill the map as a 2d Array
def populateWithInput(filename):
    with open(filename,"r") as file:
        for line in file:
            map.append(list(line.strip()))
populateWithInput("input.txt")
#Find me in the map
def findMe(map):
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] in ["^","<",">","v"]:
                return r,c
curpos = findMe(map)
#Print Map Out In A Digestible Way
def printMap(map):
    for row in map:
        print("".join(row))
def path(map, position):
    r, c = position
    steps = 0
    visit_count = {}
    while True:
        visit_count[(r, c)] = visit_count.get((r, c), 0) + 1
        if visit_count[(r, c)] >= 50:
            return float('inf')
        while r > 0 and map[r - 1][c] != "#":
            r -= 1
            steps += 1
            visit_count[(r, c)] = visit_count.get((r, c), 0) + 1
            if visit_count[(r, c)] >= 50:
                return float('inf')
            map[r][c] = "X"
        while c < len(map[0]) - 1 and map[r][c + 1] != "#":
            c += 1
            steps += 1
            visit_count[(r, c)] = visit_count.get((r, c), 0) + 1
            if visit_count[(r, c)] >= 50:
                return float('inf')
            map[r][c] = "X"
        while r < len(map) - 1 and map[r + 1][c] != "#":
            r += 1
            steps += 1
            visit_count[(r, c)] = visit_count.get((r, c), 0) + 1
            if visit_count[(r, c)] >= 50:
                return float('inf')
            map[r][c] = "X"
        while c > 0 and map[r][c - 1] != "#":
            c -= 1
            steps += 1
            visit_count[(r, c)] = visit_count.get((r, c), 0) + 1
            if visit_count[(r, c)] >= 50:
                return float('inf')
            map[r][c] = "X"
        if r == 0 or c == len(map[0]) - 1 or c == 0 or r == len(map) - 1:
            break
    return steps
originalSteps = path(map,curpos)
def bruteForceObstruction(map, cursteps):
    loopobstructions = 0
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] not in "^#":
                map_copy = copy.deepcopy(map)
                map_copy[row][col] = "#"
                newsteps = path(map_copy, curpos)
                if newsteps == float('inf'):
                    loopobstructions += 1
    return loopobstructions
print(bruteForceObstruction(map,originalSteps))
