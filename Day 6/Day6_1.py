from string import ascii_lowercase

inputFile = open("Day 6/input.txt", "r")
inputList = inputFile.read().splitlines()

groups = []
groupAnswers = []
yesCounter = 0

#For each line, if it's a value then add it to the current group, 
#if it's blank then end the current group and start a new one
for line in inputList:
    if line == "":
        groups.append(groupAnswers)
        groupAnswers = []
    
    else:
        groupAnswers.append(line)
#Do this one last time out of the for loop to capture the last entry
groups.append(groupAnswers)
groupAnswers = []

#For each group
for group in groups:
    #Reset group options
    groupOptions = list(ascii_lowercase)

    for entry in group:
        for char in entry:
            #For each char of each entry, if the char hasn't been reomved from the list yet, then remove it
            if groupOptions.count(char) == 1:
                groupOptions.remove(char)
    #The group answered yes to however many chars are not remaining
    yesCounter += 26 - len(groupOptions)

print(yesCounter)