def GetRow_BinaryTree(currRange, id, idIndex):
    #Define the new position in the range as the mid point
    rangeMid = round((currRange[0] + currRange[1])/2)

    #try to get the next character in the id
    try:
        char = id[idIndex]
    #If we get an index error then we've reached the end of the string so return out current position
    #(at the end of the string, out position will be the final row number)
    except IndexError:
        #Return the seat number all the way back up the chain
        return rangeMid

    #If the current character is a B then the current position becomes the minimum of the range
    if char == "B" or char == "R":
        currRange[0] = rangeMid
    #Else (if it's an F) our position becomes the maximum of the range
    else:
        currRange[1] = rangeMid
    
    #We have a new range so we go around again with the next character
    #currRange = []
    return GetRow_BinaryTree(currRange, id, idIndex + 1)

seatIds = []

inputFile = open("Day 5/input.txt", "r")
inputList = inputFile.read().splitlines()

#For each line, get the row number and seat number
for line in inputList:
    thisSeat = []
    thisSeat.append(GetRow_BinaryTree([0, 127], line[0:7], 0))
    thisSeat.append(GetRow_BinaryTree([0,7], line[7:10], 0))
    seatIds.append( (thisSeat[0] * 8) + thisSeat[1] )

print(max(seatIds))