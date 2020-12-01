import numpy

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

    for i in range(0, len(inputList)):
        inputList[i] = int(inputList[i])

    return inputList

thisList = GetListOfInts()
targetAnswer = 2020

for i in range(0, len(thisList)):
        for j in range(i, len(thisList)):
                for k in range(j, len(thisList)):
                    if thisList[i] + thisList[j] + + thisList[k]== targetAnswer:
                        solutions = [thisList[i], thisList[j], + thisList[k]]
                        print (f"The three numbers which sum to make {targetAnswer} are: {str(solutions)}")
                        solution_multiplied = numpy.prod(solutions)
                        print ("If you multiply them togeter, you get: " + str(solution_multiplied))

print("""
*******************************
""")