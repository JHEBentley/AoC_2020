counter_1s = 0
counter_3s = 0

inputFile = open("Day 10/input.txt", "r")
inputList = list(map(int, inputFile.read().splitlines()))
inputList.sort()
inputList.append(inputList[-1] + 3)


currJoltage = 0
for joltage in inputList:
    diffJoltage = joltage - currJoltage

    if diffJoltage == 1:
        counter_1s += 1
    elif diffJoltage == 3:
        counter_3s += 1
    
    currJoltage = joltage

print(counter_1s * counter_3s)
