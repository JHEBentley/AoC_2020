def ExecuteInstructions(instructionsList, mask):
    for instruction in instructionsList:
        instruction = instruction.split("] = ")
        #Get instruction address
        mem = instruction[0][4:]
        #Dec instruction to binary (without leading "0b"), then fill leading 0s to have a 36 bit string
        val = "{0:b}".format(int(instruction[1])).zfill(36)
        #Add masked value to the dictionary
        memory[mem] = Mask(val, mask)

def Mask(val, mask):
    newVal = ""
    for c in range(0, len(mask)):
        if mask[c] != "X":
            newVal += mask[c]
        else:
            newVal += val[c]

    return newVal

inputFile = open("Day 14/input.txt", "r")
inputList = inputFile.read().splitlines()

memory = {}
mask = inputList[0].split(" = ")[1]
inputList.remove(inputList[0])

instructionsList = []
for i, line in enumerate(inputList):
    if line[:4] == "mask":
        #There's a new mask available, so execute with what we have
        ExecuteInstructions(instructionsList, mask)
        #Assign the new mask
        mask = line.split(" = ")[1]
        #Wipe the intructions list
        instructionsList = []

    else:
        instructionsList.append(line)
#Execute one last time to ensure the last list has been processed
ExecuteInstructions(instructionsList, mask)

total = 0
for adr in memory:
    total += int(memory[adr], 2)

print(total)