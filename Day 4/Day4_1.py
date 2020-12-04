def CheckValidEntries(listOfEntries):
    #Check how many times each entry contains the required entry types
    for entryType in RequiredEntryTypes:
        if listOfEntries.count(entryType) != 1:
            return 0

    #If it makes it here without breaking, it means each type occured once so you can approve it
    return 1

RequiredEntryTypes = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
counter = 0

inputFile = open("Day 4/input.txt", "r")
inputList = inputFile.read().splitlines()

inputListFixed = []
currPassport = ""

#Get rid of the line breaks to get a new list of passports without any breaks
for line in inputList:
    if line != "":
        currPassport += (" " + line)  
    else:
        inputListFixed.append(currPassport)
        currPassport = line
inputListFixed.append(currPassport)

#For each passport
for passport in inputListFixed:
    #Get each entry
    entries = passport.split()

    #Check present entry types by putting them in a list
    presentEntries = []
    for entry in entries:
        #Get it's type and add it to the list of present types for this entry
        entryType = (entry.split(":"))[0]
        presentEntries.append(entryType)

    #Add a value to counter (0 or 1) depending on if the check function accepts it or not
    counter += CheckValidEntries(presentEntries)

print(counter)