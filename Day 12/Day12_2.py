N, E = 0, 0
way_N, way_E = 1, 10

inputFile = open("Day 12/input.txt", "r")
inputList = inputFile.read().splitlines()

for instruction in inputList:
    #Break up instruction inputs
    act = instruction[:1]
    amount = int(instruction[1:])

    if act == "F":
        N += way_N * amount
        E += way_E * amount

    if act == "N":
        way_N += amount
    elif act == "S":
        way_N -= amount
    elif act == "E":
        way_E += amount
    elif act == "W":
        way_E -= amount

    #Re-translate the waypoint's position around the ship in chunks of 90 degrees 
    #until we don't have to do anymore for this instruction
    if act == 'L':
        while amount != 0:
            way_E, way_N = -way_N, way_E
            amount -= 90
    elif act == 'R':
        while amount != 0:
            way_E, way_N = way_N, -way_E
            amount -= 90

print(abs(N) + abs(E))