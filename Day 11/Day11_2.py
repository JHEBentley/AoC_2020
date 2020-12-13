inputFile = open("Day 11/input.txt", "r")
seatList = inputFile.read().splitlines()

counter = 0

def UpdateSeats(currSeatList):
    updatedSeats = []
    for row in range(len(currSeatList)):
        updatedRow = ""
        for seat in range(len(currSeatList[0])):
            adj = GetAdjSeats(seat, row, currSeatList)
            if currSeatList[row][seat] == "L" and "#" not in adj:
                updatedRow += "#"
            elif currSeatList[row][seat] == "#" and adj.count("#") >= 5:
                updatedRow += "L"
            else:
                updatedRow += currSeatList[row][seat]
        updatedSeats.append(updatedRow)
    return updatedSeats

def GetAdjSeats(yPos, xPos, grid):
    #Gets a list of the seat values of each seat in the 8 surrounding the seat at the input
    adjSeats = []
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if x == y == 0:
                continue
            i = 1
            while 0 <= xPos+i*x < len(grid) and 0 <= yPos+i*y < len(grid[0]):
                ch = grid[xPos+i*x][yPos+i*y]
                if ch != '.':
                    adjSeats.append(ch)
                    break
                i += 1
    
    return adjSeats
    
updatedSeats = UpdateSeats(seatList)
while updatedSeats != seatList:
    seatList = updatedSeats
    updatedSeats = UpdateSeats(seatList)

for row in seatList:
    listRow = list(row)
    counter += listRow.count("#")

print(counter)