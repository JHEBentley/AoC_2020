#Improved from several hours to 0.012964 seconds

from collections import defaultdict

inputFile = open("Day 10/input.txt", "r")
inputList = list(map(int, inputFile.read().splitlines()))
inputList.sort()

#Need to add the charging outlet at position 0 with a value of 0 to form as a constant base for the dict.
#Not doing this caught me out initially because it isn't guaranteed that adapter 1 will be required in every solution, 
#or that the lowest number will even be 1 (unlike the test input where adapter 1 was used every time)
inputList.insert(0, 0)

Target = (inputList[-1] + 3)

#Attempt using defaultdict, primary learning source: https://www.accelebrate.com/blog/using-defaultdict-python
#Creates a defaultdict object which in turn is initialsed as a dictionary of ints
#If you try to access a value which is missing, rather than returning an error a default value gets returned
#By inititialising using "lambda: 0" this default value is 0
counterDict = defaultdict(lambda: 0)

#Initialise each necassery entry in the dict. with default value 0
for value in range(0, Target + 1):
    counterDict[value]

#Add our target to the dict with a value of one (as it should only occur once for every solution)
counterDict[Target] = 1

#Goes through each joltage element of the dict. and adds how many times that element + i 
#would create another valid entry (if it doesn't create any valid entries, it returns the deault of 0)
#This approach has to be top down though (hence looping through backwards) because the sums compound as we
#get further twowards the base. Looping through forwards would return 0 as the sums won't build on the entries
#higher up in the dict.
for joltage in reversed(inputList):
    #Have each element in the dict correspond to the number of valid paths they created.
    for i in range(1, 4):
        counterDict[joltage] += counterDict[joltage + i]

#Print the base value of the dict, which will be the sum of all the other dict. entries
print(counterDict[0])