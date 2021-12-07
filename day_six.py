
from typing import Counter


def textToArray(fname):


    with open(fname) as f:
        res = f.readline()

    f.close()

    return [int(v) for v in res.split(',')]



def simulatefishDict(fish):
    '''
    use dict to keep track of fish and their lifespans
    '''
    fish = Counter(fish)

    for _ in range(256):

        fish = finishOneDayDict(fish)

    return sum(fish.values())

def simulateFish(fish):
    '''
    brute force solution - works for part 1
    '''    

    for _ in range(80):
        fish = finishOneDay(fish)

    return len(fish)

def finishOneDay(fish):

    for i in range(len(fish)):
        if fish[i] == 0: #fish has died : reset that fish life to 6 and add the new fish life 8
            fish[i] = 6
            fish.append(8)

        else:
            fish[i] -= 1

    return fish


def finishOneDayDict(fish):
    new_fish = {i:0 for i in range(0,9)}

    for k,v in fish.items():
        if k == 0:
            new_fish[6] += v
            new_fish[8] += v
        
        else:
            new_fish[k-1] += v

    return new_fish

file = './data/day_six_input.txt'
print(simulatefishDict(textToArray(file)))

