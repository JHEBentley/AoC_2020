from collections import defaultdict

#Initisalise turn as turn 1
turn = 1
StartingSet = list(map(int, "9,19,1,6,0,5,4".split(",")))
#Dict of numbers that have been spoken, where the value is the last turn they were spoken
SpokenNumbers = defaultdict(int)
lastNumber = StartingSet[0]

for i, num in enumerate(StartingSet):
    if i == 0:
        continue
    SpokenNumbers[lastNumber] = [turn, 0]
    lastNumber = num
    turn += 1

while turn != 2020:
    #Initialise the number this player will say
    numberToSay = 0
    
    if SpokenNumbers[lastNumber] == 0:
        numberToSay = 0
        SpokenNumbers[lastNumber] = [turn, 0]
    else:
        numberToSay = (SpokenNumbers[lastNumber][0] - SpokenNumbers[lastNumber][1])

    turn += 1
    try:
        SpokenNumbers[numberToSay] = [turn, SpokenNumbers[numberToSay][0]]
    except TypeError:
        #This will be handled on the next turn when the dict value is found to be 0
        pass

    lastNumber = numberToSay

print(numberToSay)