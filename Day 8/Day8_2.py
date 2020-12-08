accumulator = 0
indexSeenBefore = []

inputFile = open("Day 8/input.txt", "r").read().split()
instructionList = []
newInstruction = []
index = 0
for line in inputFile:
    newInstruction.append(line)
    #If we've reached the increment, then that's the last entry per instruction so start making a new one
    if line[0] == "+" or line[0] == "-":
        #Give it an index
        newInstruction.append(index)
        index += 1

        instructionList.append(newInstruction)
        newInstruction = []

def SwapVars(var):
    if var == "nop":
        return "jmp"
    elif var == "jmp":
        return "nop"
    else:
        return "acc"

def BruteForceApproach(instruction, accumulator):
    currIndex = instructionList.index(instruction)
    #If we haven't seen see this index before then we can continue, but if we have then we're looping so
    # this path does not end, so it has failed
    if indexSeenBefore.count(currIndex) == 0:
        indexSeenBefore.append(currIndex)
    else:
        return False

    if instruction[0] == "nop":
        nextIndex = currIndex + 1

    elif instruction[0] == "acc":
        if instruction[1][0] == "+":
            accumulator += int(instruction[1][1:])
        else:
            accumulator += int(instruction[1])

        nextIndex = currIndex + 1

    elif instruction[0] == "jmp":
        if instruction[1][0] == "+":
            nextIndex = currIndex + int(instruction[1][1:])
        else:
            nextIndex = currIndex + int(instruction[1])

    #If we get an index error when trying to progress then we made it to the end, so return the accumulator
    try:
        return BruteForceApproach(instructionList[nextIndex], accumulator)
    except IndexError:
        return accumulator

for instr in instructionList:
    #Brute force loop through each intstruction and change nops to jmps and jmps to nops
    instr[0] = SwapVars(instr[0])
    result = BruteForceApproach(instructionList[0], accumulator)
    if result == False:
        #Function started looping so failed.
        #Reset the seen before list and instruction.
        indexSeenBefore = []
        instr[0] = SwapVars(instr[0])
    else:
        #We didn't get a fail so we must have got the accumulator value. We can stop the for loop now.
        print(result)
        break