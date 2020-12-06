from string import ascii_lowercase

def IsCharPresent(c, group):
    for entry in group:
        #If the char isn't present then the group as a whole does not contain this answer
        if c not in entry:
            return False
    
    #If we've made it this far, then each entry in this group does contain an instance of this char
    return True

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

#For each group
for group in groups:
    #Reset group options
    groupOptions = []

    #For each character in the alphabet
    for char in ascii_lowercase:
        #If this function returns true, then add it to the list of present chars
        if IsCharPresent(char, group):
            groupOptions.append(char)

    yesCounter += len(groupOptions)

print(yesCounter)