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

def ExecuteInstruction(instruction, accumulator):
    currIndex = instructionList.index(instruction)
    #If we haven't seen see this index before then we can continue, but if we have then we're looping so
    #return where the accumulator is at currently
    if indexSeenBefore.count(currIndex) == 0:
        indexSeenBefore.append(currIndex)
    else:
        return accumulator

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

    return ExecuteInstruction(instructionList[nextIndex], accumulator)

print(ExecuteInstruction(instructionList[0], accumulator))