import re

def GetListOfInts():
    inputList = []

    print("Please enter your values below:")
    print("""
    *******************************
    """)

    while True:
        line = input()
        if line:
            inputList.append(line)
        else:
            break

    return inputList

def ExtractRule(index):
    #Uses regex to extract a list of the integers found in a given rule
    rule = ([int(num) for num in re.findall(r"\d+", rulesList[index])])
    #Extracts the last char from the rules string, which will always be the letter
    rulesLet = (rulesList[index])[-1]

    rule.append(rulesLet)

    #Returns the rule as a list in the format (int, int, letter)
    return rule

newList = GetListOfInts()
rulesList = []
passwordsList = []
counter = 0

#Splits input into a list of the rules and their corresponding passwords
for i in range(0, len(newList)):
    splitList = newList[i].split(": ")
    rulesList.append(splitList[0])
    passwordsList.append(splitList[1])

for i in range(0, len(newList)):
    #Take the rule at the current index as the current rule to focus on
    currentRule = ExtractRule(i)

    #Split the corresponding password into a list of chars
    passwordElements = list(passwordsList[i])

    #Subtract 1 from each rule position (as the index zero is not adhered to)
    currentRule[0] -= 1
    currentRule[1] -= 1

    #if the letter of the rule occurs in one of the poitions then add to counter
    if(passwordElements[currentRule[0]] == currentRule[2] or passwordElements[currentRule[1]] == currentRule[2]):
        counter += 1

    #if the letter occurs in both of the positions (which is not allowed) then subtract what was just added
    if(passwordElements[currentRule[0]] == currentRule[2] and passwordElements[currentRule[1]] == currentRule[2]):
        counter -= 1

print (counter)