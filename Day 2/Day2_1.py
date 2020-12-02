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

    #If the count of the current tule's letter in the corresponsing password is within the constraints then add it to the counter
    if (currentRule[0] <= passwordsList[i].count(currentRule[2]) <= currentRule[1]):
        counter += 1

print (counter)