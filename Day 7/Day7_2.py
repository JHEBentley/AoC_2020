def GetBagCount(bag):
    counter = 0

    #For each item in this bag, find how many bags are contained within recursively 
    for item in bagTypes[bag]:
        print(int(item[0]))
        counter += int(item[0]) + int(item[0]) * GetBagCount(item[1])

    return counter

#Create a dictionary called bagTypes
bagTypes = {}
targetBag = "shiny gold"
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
    bagTypes[bag] = thisBagsContents

print(GetBagCount(targetBag))