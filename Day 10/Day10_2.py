from datetime import datetime

now = datetime.now()

counter = 0

inputFile = open("Day 10/input.txt", "r")
inputList = list(map(int, inputFile.read().splitlines()))
inputList.sort()
Target = (inputList[-1] + 3)
print(Target)

def CombinationFinder(currJoltage):
    global counter
    for i in range(1,4):
        testIncrement = currJoltage + i
        #If adding by this increment is valid
        if testIncrement == Target:
            counter += 1
            break
        elif inputList.count(testIncrement) == 1:
            CombinationFinder(testIncrement)
        elif testIncrement > Target:
            break

CombinationFinder(0)
print(counter)

#I wanted to see how long this would take, the answer was too long...
duration = datetime.now() - now
print(duration.total_seconds())