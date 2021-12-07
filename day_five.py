#day five

def textToArray(fname):

    lines = []

    with open(fname) as f:
        for line in f:
            #print(line.split('->'))
            pt1, pt2 = line.strip().split('->')
            lines.append([[int(pt) for pt in pt1.split(',')], [int(pt) for pt in pt2.split(',')]])

    f.close()

    return lines

def isHorizontal(line):
    return line[0][0] == line[1][0]
    
def getVertHoriLines(lines):

    valid_lines = []
    diag_lines = []

    for pt1, pt2 in lines:
        if pt1[0] == pt2[0] or pt1[1] == pt2[1]:
            valid_lines.append([pt1, pt2])

        #part 2
        else:
            diag_lines.append([pt1, pt2])

    return valid_lines,diag_lines

def getIntersectCount(lines):

    #if the vertical line's x coord is between horizontal lines x coords of both points AND if v's lowest point is below the y coord of th
    return isHorizontal(lines[-1])

def makeGridSol(st_lines, d_lines):

    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    #draw the straight lines
    for line in st_lines:
        if isHorizontal(line):
            x = line[0][0]
            start = min(line[0][1], line[1][1])
            end = max(line[0][1], line[1][1])

            for i in range(start, end+1):
                grid[x][i] += 1

        else:
            y = line[0][1]
            start = min(line[0][0], line[1][0])
            end = max(line[0][0], line[1][0])

            for i in range(start, end+1):
                grid[i][y] += 1

    #draw the diagonal lines
    for line in d_lines:
        pt1, pt2 = sorted(line, key = lambda x : x[1]) #sort on the second elements (y pos)
        if pt1[0] < pt2[0]:
            i, j = pt1
            while i <= pt2[0] and j <= pt2[1]:
                grid[i][j] += 1
                i += 1
                j += 1

        else:
            i,j = pt1
            #j is increasing, i is decreasing
            while i >= pt2[0] and j <= pt2[1]:
                grid[i][j] += 1
                i -= 1
                j += 1


    return grid

def findOverlapCount(mat):

    count = 0

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] >= 2:
                count += 1

    return count

file = './data/day_five_input.txt'

st_lines, diag_lines = getVertHoriLines(textToArray(file))
print(findOverlapCount(makeGridSol(st_lines, diag_lines)))


