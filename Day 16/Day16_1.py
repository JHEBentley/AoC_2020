def AddRule(rule, ruleDict):
    spRule = rule.split(": ")
    ruleName = spRule[0]
    ruleRange = spRule[1].split(" or ")
    #Add each rule by name to the dict, with two tuples for each of the rule's ranges
    ruleDict[ruleName] = [tuple(map(int, x.split("-"))) for x in ruleRange]

def CheckValidity(rules):
    for rule in rules:
        for _range in rules[rule]:
            #Check if the given value is within ANY of the ranges given, if so, it is valid
            if value in range(_range[0], _range[1] + 1):
                return True
    #If we make it this far, then we haven't fund any valid matches so it must be invalid
    return False

inputFile = open("Day 16/input.txt", "r")
inputList = inputFile.read().splitlines()

rules = {}
myTicket = []
nearbyTickets = []
validValues = []
invalidValues = []

region = 0
for line in inputList:
    if line == "":
        region += 1
        continue

    #Stops the section headers getting added 
    if line[-1] != ":":
        if region == 0:
            AddRule(line, rules)
        elif region == 1:
            newVal = []
            for value in line.split(","):
                newVal.append(int(value))
            myTicket.append(newVal)
        elif region == 2:
            newVal = []
            for value in line.split(","):
                newVal.append(int(value))
            nearbyTickets.append(newVal)

for ticket in nearbyTickets:
    for value in ticket:
        if CheckValidity(rules) == False:
            invalidValues.append(value)
            continue
        
print(sum(invalidValues))