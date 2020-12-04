def CheckValidEntries(listOfEntries):
    #Check how many times each entry contains the required entry types
    for entryType in RequiredEntryTypes:
        if listOfEntries.count(entryType) != 1:
            return 0

    #If it makes it here without breaking, it means each type occured once so you can approve it
    return 1

def CheckFormatIsOkay(entryType, value):
    if entryType == "ecl":
        validEyeColours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        #If any on the valid colours occur once, and only once
        if validEyeColours.count(value) == 1:
            return True
    elif entryType == "pid":
        if len(value) == 9:
            return True
    elif entryType == "eyr":
        if len(value) == 4 and 2020 <= int(value) <= 2030:
            return True
    elif entryType == "hcl":
        #Must start with a #
        if value[0] == "#" and len(value) == 7:
            try:
                #Try to convert the value (minus the #) from hex to dec
                int(value[-1], 16)
            except ValueError:
                #This number is not a hex number, so return false
                return False
            #We made it through, so return true
            return True
    elif entryType == "byr":
        if len(value) == 4 and 1920 <= int(value) <= 2002:
            return True
    elif entryType == "iyr":
        if len(value) == 4 and 2010 <= int(value) <= 2020:
            return True
    elif entryType == "hgt":
        lastTwoLetters = value[-2] + value[-1]
        if lastTwoLetters == "cm":
            if 150 <= int(value[:-2]) <= 193: #[:-2] removes the last two chars from a string
                return True
        elif lastTwoLetters == "in":
            if 59 <= int(value[:-2]) <= 76: #[:-2] removes the last two chars from a string
                return True
    #Else, it doesn't have conditions so approve it blind, if it's wrong then it won't get found later anyway
    else:
        return True

    #The entry was accepted into one of the if statements but was not passed, 
    #therefore it must be failed
    return False

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
        entryValue = (entry.split(":"))[1]

        #Run check on differnt entry types, if they aren't valid here 
        #then don't bother adding them and it'll fail later on
        if CheckFormatIsOkay(entryType, entryValue):
            presentEntries.append(entryType)

    #Add a value to counter (0 or 1) depending on if the check function accepts it or not
    counter += CheckValidEntries(presentEntries)

print(counter)