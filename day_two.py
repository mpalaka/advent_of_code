#day two: calculate the position of the submarine

def textToArray(fname):

    depth_ar = []

    with open(fname) as f:
        for line in f:
            depth_ar.append(line.strip())

    f.close()
    
    return depth_ar

#part one
def findPos(commands):
    x,y = 0,0

    for cmd in commands:
        ins, val = cmd[0], int(cmd[-1])

        if ins == 'f':
            x += val

        elif ins == 'u':
            y -= val

        else:
            y += val

    return x*y

#part two
def findPosAim(commands):
    x = 0
    y = 0
    aim = 0

    for cmd in commands:
        ins, val = cmd[0], int(cmd[-1])

        if ins == 'f':
            x += val
            y = y + aim*val

        elif ins == 'u':
            aim -= val

        else:
            aim += val

    return x*y

fname = './data/day_two_input.txt'
print(findPos(textToArray(fname)))