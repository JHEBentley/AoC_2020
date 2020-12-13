def CalculateContiguousSeq(busses):
    #Initialse busIDs multiplied as 1
    totBusIDs = 1

    time = 0

    #Multiply busIDs together
    for bus in busses:
        totBusIDs *= bus[1]

    for bus in busses:
        tempTime = totBusIDs // bus[1]
        time += bus[0] * tempTime * pow(tempTime, bus[1] - 2, bus[1])
        time %= totBusIDs
        
    return time

inputFile = open("Day 13/input.txt", "r")
lines = inputFile.read().splitlines()

Busses = lines[1].split(",")

listOfBusses = []
#Build in an index using enumerate
for busIndex, busID in enumerate(Busses):
    if busID != "x":    
        busID = int(busID)
        listOfBusses.append([busID - busIndex, busID])

print(CalculateContiguousSeq(listOfBusses))