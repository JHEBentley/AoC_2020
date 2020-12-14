from itertools import product

def ExecuteInstructions(instructionsList, mask):
    for instruction in instructionsList:
        instruction = instruction.split("] = ")
        #Get instruction address
        mem = "{0:b}".format(int(instruction[0][4:])).zfill(36)
        #Dec instruction to binary (without leading "0b"), then fill leading 0s to have a 36 bit string
        val = "{0:b}".format(int(instruction[1])).zfill(36)
        
        #Get the list of masked memory addresses
        newMems = Mask(mem, mask)
        for mem in newMems:
            #Add masked value to the dictionary
            memory[mem] = val

def Mask(adr, mask):
    newAdrList = []
    finalAdrList = []
    #New mask rules
    for c in range(0, len(mask)):
        if mask[c] != "0":
            newAdrList.append(mask[c])
        else:
            newAdrList.append(adr[c])

    #Itertools product generates a list of tuples which efectively ac as a truth table
    TruthOptions = list(product(range(2), repeat=newAdrList.count("X")))
    for option in TruthOptions:
        index = 0
        adrss = list(newAdrList)
        #For each occurance of an X in the address, replace it by cycling through the truth table options
        for i, c in enumerate(adrss):
            if c == "X":
                adrss[i] = option[index]
                index += 1
        
        #Remake the address string and append it to the list to be returned
        finalAdrList.append(int("".join(str(x) for x in adrss), 2))

    return finalAdrList

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