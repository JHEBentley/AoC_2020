import numpy

def GetActiveNeighbourCount(cubes):
    activeCounter = 0

    #Cycle through all possible neighbours and add to counter if they are active
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                #Ignore self
                if i == 0 and j == 0 and k == 0:
                    continue
                if 0 <= x + i < cubes.shape[0] and 0 <= y + j < cubes.shape[1] and 0 <= z + k < cubes.shape[2]:
                    if cubes[x + i][y + j][z + k] == "#":
                        activeCounter += 1

    return activeCounter

def GetNewCubes(activeCounter, oldCubes):
    if oldCubes == "#" and activeCounter not in [2, 3]:
        return "." 
    else:
        if oldCubes == "." and activeCounter == 3:
            return "#"  
        else: 
            return oldCubes

numOfCycles = 6

inputFile = open("Day 17/input.txt", "r")
inputList = inputFile.read().splitlines()

cubes = numpy.array([list(cube) for cube in inputList])
#Use numpy.newaxis to covert from a 1D to 2D, then 2D to 3D (hence the :, :, numpy.newaxis)
#https://stackoverflow.com/questions/29241056/how-does-numpy-newaxis-work-and-when-to-use-it
cubes = cubes[:, :, numpy.newaxis]

cycles = 0
while cycles < numOfCycles:
    #Simulate empty edges of the dimension by using the pad function to fill the edges with
    #inactive cubes. numpy.pad is a far better way of doing this than I used before.
    cubes = numpy.pad(cubes, ((1, 1), (1, 1), (1, 1)), constant_values=".")
    newCubes = numpy.copy(cubes)

    #Using numpy.newaxis creates sub elements of the array called shapes, which in this case
    #correspond to the x, y, and z of the elements in the array.
    for x in range(cubes.shape[0]):
        for y in range(cubes.shape[1]):
            for z in range(cubes.shape[2]):
                activeCounter = GetActiveNeighbourCount(cubes)
                oldCubes = cubes[x][y][z]
                newCubes[x][y][z] = GetNewCubes(activeCounter, oldCubes)

    #Update cubes
    cubes = newCubes

    cycles += 1

print(sum([1 for x in cubes for y in x for z in y if z == "#"]))