def ExtractParenthesis(problem):
    for c in problem:
        #Extract any contents between the last remaining "(" and it's corresponding ")"
        extractedOG = problem[problem.rfind("(")+1:problem.find(")", problem.rfind("(")+1)]
        extractedNew = extractedOG
        for c in extractedOG:
            if c == "(":
                #Replace the extracted maths with the solution to that maths (as it will have been passed
                #through the "DoMaths" function)
                extractedNew = ExtractParenthesis(extractedOG)
                continue

        #Replace the extracted segment of the string with the mathematical solution
        problem = problem.replace("("+extractedOG+")", str(DoMaths(extractedNew)))
    return problem

def DoMaths(problem):
    currAct = "+"
    answer = 0
    problemSep = problem.split(" ")
    for c in problemSep:
        if c.isnumeric():
            c = int(c)
            if currAct == "+":
                answer += c
            elif currAct == "*":
                answer *= c
        else:
            currAct = c
                
    return answer

inputFile = open("Day 18/input.txt", "r")
inputList = inputFile.read().splitlines()

answerList = []
for problem in inputList:
    answerList.append(DoMaths(ExtractParenthesis(problem)))

print(sum(answerList))