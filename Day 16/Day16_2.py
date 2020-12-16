from collections import defaultdict
import math

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

def CheckOptions(value, rules):
    validRules = []
    for rule in rules:
        for _range in rules[rule]:
            if value in range(_range[0], _range[1] + 1) and validRules.count(rule) == 0:
                validRules.append(rule)
                
    return validRules

def RemoveThisOption(positionOptions, index, optionToRemove):
    for i in positionOptions:
        if i != index and optionToRemove in positionOptions[i]:
            positionOptions[i].remove(optionToRemove)

inputFile = open("Day 16/input.txt", "r")
inputList = inputFile.read().splitlines()

rules = {}
myTicket = []
nearbyTickets = []
invalidTickets = []

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

#Find invalid tickets and then remove from the list of nearby tickets as they are now irrelevant
for ticketID, ticket in enumerate(nearbyTickets):
    for value in ticket:
        if CheckValidity(rules) == False:
            invalidTickets.append(ticketID)
            continue
#Sorted and reversed invalid IDs so as not to mess with the list index
for ticketID in reversed(sorted(invalidTickets)):
    nearbyTickets.remove(nearbyTickets[ticketID])

#Initialise a dict which assumes every value could be any of the given rules by default
positionOptions = defaultdict(lambda: [rule for rule in rules])

for ticket in nearbyTickets:
    for i, value in enumerate(ticket):
        existingOptions = positionOptions[i]
        #Reduce the options to only the options which are already present, and the ones that were just returned
        #(this prevents duplication or options being added back in)
        positionOptions[i] = set(existingOptions).intersection(CheckOptions(value, rules))

#At least one of the dict entries must now only have one value, so remove this value from all other dict entries
#Keep looping and doing that until all of the entries only have one possible option
while any((len(positionOptions[i]) > 1) for i in positionOptions):
    for i in positionOptions:
        if len(positionOptions[i]) == 1:
            elementToRemove = list(positionOptions[i])[0]
            RemoveThisOption(positionOptions, i, elementToRemove)

#Add all values from my ticket which are in the position indicating they are to do with departure to a list
departureValues = []
for i in positionOptions:
    if list(positionOptions[i])[0][:9] == "departure":
        departureValues.append(myTicket[0][int(i)])

print(math.prod(departureValues))