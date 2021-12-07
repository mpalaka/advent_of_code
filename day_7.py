#day 7

def textToArray(fname):
    with open(fname) as f:
        res = f.readline()

    f.close()

    return [int(v) for v in res.split(',')]

def findMinCostBrute(nums):
    min_cost = float('inf')
    nums.sort()
    max_val = nums[-1]

    for i in range(max_val):
        #print(f'move all crabs to {i}')
        #change all the numbers to nums[i] and find cost
        temp_sum = 0
        for num in nums:
            diff = abs(num-i)
            if diff > 0:
                temp_sum += sumN(diff)

            #print(f'{num} : {sumN(diff)}')
            
        min_cost = min(min_cost, temp_sum)

    return min_cost

#for pt 2
def sumN(num):
    return (num*(num+1))//2


file = './data/day_7_ip.txt'

print(findMinCostBrute(textToArray(file)))

# file = [16,1,2,0,4,2,7,1,2,14]
# print(findMinCostBrute(file))