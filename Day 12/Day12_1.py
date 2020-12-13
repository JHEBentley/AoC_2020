N, E = 0, 0
bearing = 90

inputFile = open("Day 12/input.txt", "r")
inputList = inputFile.read().splitlines()

for instruction in inputList:
    #Break up instruction inputs
    act = instruction[:1]
    amount = int(instruction[1:])

    #Forward is the equivalent of an NEWS movements based on the ship's bearing
    if act == "F":
        if bearing == 0:
            act = "N"
        elif bearing == 90:
            act = "E"
        elif bearing == 180:
            act = "S"
        elif bearing == 270:
            act = "W"

    if act == "N":
        N += amount
    elif act == "S":
        N -= amount
    elif act == "E":
        E += amount
    elif act == "W":
        E -= amount

    elif act == "L":
        bearing -= amount
    elif act == "R":
        bearing += amount

    #Make sure the bearing stays between 0 and 259 degrees
    if bearing >= 360:
        bearing -= 360
    elif bearing < 0:
        bearing += 360

print(abs(N) + abs(E))