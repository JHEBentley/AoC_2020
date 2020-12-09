preambleLength = 25

inputFile = open("Day 9/input.txt", "r")
#Remaped input from str to ints to make later maths easier
remapInput = map(int, inputFile.read().splitlines())
inputList = list(remapInput)

def FindInvalidStep(id):
    currTarget = inputList[id]

    #Get the current preamble in a list
    thisPreAm = []
    for preAm in range(id - preambleLength, id):
        thisPreAm.append(inputList[preAm])

    #Check if any of the unique numbers in the preamble sum to make the target, if so then we can proceed
    for preAm in thisPreAm:
        for num in thisPreAm:
            if preAm != num and (currTarget == int(preAm) + int(num)):
                return FindInvalidStep(id + 1)

    #If not then return the current target, as none of the preamble numbers can sum to make it
    return currTarget

print(FindInvalidStep(preambleLength))