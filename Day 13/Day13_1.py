import numpy

def GetNextBus(timeTable, Target):
    timeTable = numpy.asarray(timeTable)
    
    nextBusID = (numpy.abs(timeTable - Target)).argmin()

    #Next bus has to be after the target time, can't be before
    if timeTable[nextBusID] < Target:
        return timeTable[nextBusID + 1]
    else:
        return timeTable[nextBusID]

inputFile = open("Day 13/input.txt", "r")
inputList = inputFile.read().splitlines()

Target = int(inputList[0])
splitList = inputList[1].split(",")
Busses = []
for c in splitList:
    if c != "x":
        Busses.append(int(c))

nextBusses = []
for busID in Busses:
    timeTable = []
    for time in range(busID, Target + busID, busID):
        timeTable.append(time)

    nextBusses.append(GetNextBus(timeTable, Target))

nextBus = min(nextBusses)
#Get the ID of the nex bus based on it's position in the nextBusses list
nextBusID = Busses[nextBusses.index(nextBus)]
print((nextBus - Target) * nextBusID)