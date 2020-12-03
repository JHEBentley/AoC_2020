def Move(currentPos, step):
    newPos = [(currentPos[0] + step[0]), (currentPos[1] + step[1])]

    #The map repeats itself horizontally, so if we exceed the horizontal bounds we can 
    #jump back by one whole width
    #Check against the map width - 1 due to index zero
    if newPos[0] > mapDimensions[0] - 1:
        newPos[0] -= mapDimensions[0]

    return newPos
  
def CalculateHazards(position, step):
    counter = 0

    while position[1] < mapDimensions[1] - 1:
        position = Move(position, step)

        x = position[0]
        y = position[1]

        print(position)
        mapPos = inputList[y][x]
        if mapPos == hazardSymbol:
            counter += 1
    
    return counter

step = [3,1]
startPosition = [0,0]
spaceSymbol = "."
hazardSymbol = "#"

#I found an easier way to split an input directly from a text file...
inputFile = open("Day 3/input.txt", "r")
inputList = inputFile.read().splitlines()

#Get width and height of the map and define how we're going to move through it
mapDimensions = (len(inputList[0]), len(inputList))

print(CalculateHazards(startPosition, step))