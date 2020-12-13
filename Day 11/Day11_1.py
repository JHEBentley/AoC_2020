inputFile = open("Day 11/input.txt", "r")
inputList = inputFile.read().splitlines()

#Add floor to the ends of each row
seatList = ["." * (len(inputList[0]) + 2)]
for line in inputList:
    line = "." + line + "."
    seatList.append(line)
seatList.append("." * (len(inputList[0]) + 2))

#Get size of our seating area
maxX = len(seatList[0])
maxY = len(seatList)

counter = 0

def UpdateSeats(currSeatList, maxY, maxX):
    updatedSeats = []
    for row in range(0, maxY):
        updatedRow = ""
        for seat in range(0, maxX):
            thisSeat = currSeatList[row][seat]
            adj = GetAdjSeats(row, seat)

            if thisSeat == "L":
                if adj.count("#") == 0:
                    updatedRow += "#"
                else:
                    updatedRow += thisSeat
            elif thisSeat == "#":
                if adj.count("#") >= 4:
                    updatedRow += "L"
                else:
                    updatedRow += thisSeat
            else:
                updatedRow += "."
        updatedSeats.append(updatedRow)

    return updatedSeats

def GetAdjSeats(yPos, xPos):
    #Gets a list of the seat values of each seat in the 8 surrounding the seat at the input
    adjSeats = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                try:
                    adjSeats.append(seatList[yPos + i][xPos + j])
                except IndexError:
                    pass
    
    return adjSeats

while UpdateSeats(seatList, maxY, maxX) != seatList:
    seatList = UpdateSeats(seatList, maxY, maxX)

for row in seatList:
    listRow = list(row)
    counter += listRow.count("#")

print(counter)