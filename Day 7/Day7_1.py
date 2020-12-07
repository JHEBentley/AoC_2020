def CheckIfContainsTarget(dictionaryData, dictionary):
    #for the contents of the bag of this dictionary entry
    for contents in dictionaryData:
        try:
            #cycle through each type of bag this bag can contain
            for item in contents:
                #if it can contain the target bag then problem solved, this dictionary entry is valid!
                if item[1] == targetBag:
                    return True
                #if on this occasion it doesn't state that the target bag can be contained directly, see if
                #this bag has any children which can, and if so then return that the parent bag is valid.
                else:
                    if CheckIfContainsTarget(dictionary[item[1]], dictionary) == True:
                        return True
        #This means the bool attribute can be skipped over
        except TypeError:
            pass
    
    #If we made it this far, none of paths for this dictionary entry reached a target bag, so this is not valid.
    return False
    
#Create a dictionary called bagTypes
bagTypes = {}
targetBag = "shiny gold"
counter = 0
validBags = []

inputFile = open("Day 7/input.txt", "r")
#Build the contents of the dictionary
for line in inputFile:
    thisBagsContents = []
    #Removes the fullstop
    line = line[:-2]

    thisBag = line.strip("\n").split(" bags contain ")
    #Defines the bag
    bag = thisBag[0]
    #Defines the list of required contents for this bag
    contents = thisBag[1].split(", ")

    for items in contents:
        requirement = items.split(" bags")
        #This assumes the amount won't exceed 10, which it doesn't for the given input
        childAmount = requirement[0][0]
        childType = requirement[0][2:]
        #Remove any hanging occurances of the word "bag"
        if childType[-3:] == "bag":
            childType = childType[:-4]

        #Define in the list what this bag must contain and how many in a list, but not if the amount = n,
        #as this means the result was "no other bags", so there's no need to add it to the dictionary
        if childAmount != "n":
            thisBagsContents.append([childAmount, childType])

    #Add the info from this line in to the dictionary in the format {'BagType': [['amountOfChild', 'child'] bool],
    #The bool is initiated here to serve as data later on as to whether this bag is viable or not
    bagTypes[bag] = [thisBagsContents, False]

for bag in bagTypes:

    #Assign the viability bool based on contents check
    bagTypes[bag][1] = CheckIfContainsTarget(bagTypes[bag], bagTypes)

    #Count how many bags are viable
    if bagTypes[bag][1] == True:
        counter += 1

print(counter)