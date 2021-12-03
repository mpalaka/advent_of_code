#day one - check if there is an increase or decrease in the depth

#part1
def countIncrease(depths):

    inc_count = 0 

    for i in range(1,len(depths)):
        if depths[i] > depths[i-1]:
            inc_count += 1

    return inc_count

#part2
def countIncreaseWindow(depths):

    inc_count = 0

    for i in range(1,len(depths)-2):
        if sum(depths[i:i+3]) > sum(depths[i-1:i+2]):
            inc_count += 1

    return inc_count

def textToArray(fname):

    depth_ar = []

    with open(fname) as f:
        for line in f:
            depth_ar.append(int(line.strip()))

    f.close()
    
    return depth_ar

file = './data/day_one_input.txt'
print(countIncreaseWindow(textToArray(file)))