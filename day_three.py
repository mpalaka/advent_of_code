#day three - diagnostic report 

def textToArray(fname):

    depth_ar = []

    with open(fname) as f:
        for line in f:
            depth_ar.append(line.strip())

    f.close()
    
    return depth_ar

#part one
def findPowerConsumption(ar):

    one_count, zero_count = 0,0

    bit_size = len(ar[0])
    gamma = ''
    epsilon = ''

    for bit in range(bit_size):
        one_count, zero_count = 0,0
        for i in range(len(ar)):
            if ar[i][bit] == '0':
                zero_count += 1
            else:
                one_count += 1

        if zero_count > one_count:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    return int(gamma,2)*int(epsilon,2)

#part two
def findLifeSupportRating(ar):

    bit_size = len(ar[0])
    oxy, scrub = ar,ar

    #calculate the oxygen generator rating
    for bit in range(bit_size):
        one_count, zero_count = 0,0
        for i in range(len(oxy)):
            if oxy[i][bit] == '0':
                zero_count += 1
            else:
                one_count += 1

        if zero_count > one_count:
            #remove values that dont have 0
            oxy = removeVals(oxy, bit, '0')

        else:
            #remove values that dont have 1
            oxy = removeVals(oxy, bit, '1')

        if len(oxy) == 1:
            break

    #calculate the co2 scrubber rating
    for bit in range(bit_size):
        one_count, zero_count = 0,0
        for i in range(len(scrub)):
            if scrub[i][bit] == '0':
                zero_count += 1
            else:
                one_count += 1

        if one_count < zero_count:
            #remove values that dont have 1
            scrub = removeVals(scrub, bit, '1')

        else:
            #remove values that dont have 0
            scrub = removeVals(scrub, bit, '0')

        if len(scrub) == 1:
            break

    print(oxy, scrub)

    return int(scrub[0],2)*int(oxy[0],2)


def removeVals(ar,pos,val):

    to_remove = []
    #find the indices of all the numbers to be removed
    for i in range(len(ar)):
        if ar[i][pos] != val:
            to_remove.append(i)

    #create a new list, which excludes the numbers that do not meet the criteria
    new_list = [ar[i] for i in range(len(ar)) if i not in to_remove]

    return new_list

sample = ['00100',
'11110',
'10110',
'10111',
'10101',
'01111',
'00111',
'11100',
'10000',
'11001',
'00010',
'01010']

file = './data/day_three_input.txt'
print(findLifeSupportRating(textToArray(file)))
#print(scrubber(sample))