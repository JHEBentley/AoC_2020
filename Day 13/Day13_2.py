def CalculateContiguousSeq(busses):
    #Initialse busIDs multiplied as 1
    totBusIDs = 1

    time = 0

    #Multiply busIDs together
    for bus in busses:
        totBusIDs *= bus[1]

    #Chinese Remainder Theory because that's what everyone else recommended and my brute force approach took too long.
    #If I get time I'd like to come back and have another approach which is more in my style.
    for bus in busses:
        tempTime = totBusIDs // bus[1]
        time += bus[0] * tempTime * pow(tempTime, bus[1] - 2, bus[1])
        time %= totBusIDs
        
    return time

inputFile = open("Day 13/input.txt", "r")
inputList = inputFile.read().splitlines()

Busses = inputList[1].split(",")

listOfBusses = []
#Build in an index using enumerate
for busIndex, busID in enumerate(Busses):
    if busID != "x":    
        busID = int(busID)
        listOfBusses.append([busID - busIndex, busID])

print(CalculateContiguousSeq(listOfBusses))