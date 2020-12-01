def GetListOfInts():
    inputList = []

    print("Please enter your values below:")
    print("*******************************")

    while True:
        line = input()
        if line:
            inputList.append(line)
        else:
            break

    for i in range(0, len(inputList)):
        inputList[i] = int(inputList[i])

    return inputList

thisList = GetListOfInts()
targetAnswer = 2020

for i in range(0, len(thisList)):
        for j in range(i, len(thisList)):
            if thisList[i] + thisList[j] == targetAnswer:
                solutions = [thisList[i], thisList[j]]
                print (f"The two numbers which sum to make {targetAnswer} are: {str(solutions[0])} and {str(solutions[1])}")
                solution_multiplied = solutions[0] * solutions[1]
                print ("If you multiply them togeter, you get: " + str(solution_multiplied))

print("*******************************")