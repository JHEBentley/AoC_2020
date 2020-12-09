Target = 375054920

inputFile = open("Day 9/input.txt", "r")
inputList = list(map(int, inputFile.read().splitlines()))

def encryptionSum():
    #For each element in the input list, keep summing the next number
    for i in range(0, len(inputList)):
        runningTotal = 0
        solutions = []
        #For each number on from the current element
        for j in range(i, len(inputList)):
            #If the running total is less than the target, this could still potentially be a set of soltuions, 
            #so add to the solution set and increment the running total
            if runningTotal < Target:
                runningTotal += inputList[j]
                solutions.append(inputList[j])

            #If the running total equals the target, then this is our solution set
            elif runningTotal == Target:
                return(solutions)

            #We've passed the target, so this is not our set of solutions.
            #Break the for loop, reset the count and solutions, and start again from the next element in the input list.
            else:
                break

solutionSet = encryptionSum()
print(min(solutionSet) + max(solutionSet))