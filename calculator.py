def parseList(strExpression): #Function combines adjacent numbers and decimals together
    exprList = list(strExpression)
    count = -1
    for index in exprList:
        count += 1
        if index != "+" and index != "-" and index != "*" and index != "/" and index != "(" and index != ")":
        #Continues if the character is not an operator
            while count < len(exprList)-1:
                while count < len(exprList)-1 and exprList[count+1] != "+" and exprList[count+1] != "-" \
                      and exprList[count+1] != "*" and exprList[count+1] != "/" and exprList[count+1] != "(" and exprList[count+1] !=")" \
                      and exprList[count] != "+" and exprList[count] != "-" \
                      and exprList[count] != "*" and exprList[count] != "/" and exprList[count] != "(" and exprList[count] !=")":
                      #Continues if the number and the number in front is not an operator
                    num = exprList[count]
                    num += exprList[count+1]
                    num = "".join(num)
                    exprList[count] = num 
                    del exprList[count+1]
                if exprList[count] == "(" or exprList[count] == ")" or exprList[count] == "+" or exprList[count] == "-" \
                      or exprList[count] == "*" or exprList[count] == "/" or exprList[count] == "(" or exprList[count] ==")":
                   count += 1
                else:
                   count += 2

    return exprList

def lenInOpenBracket(firstIndex, expressionList): 
#Function returns length of the items within brackets when an open bracket is seen
    count = firstIndex
    openBrCount = 1
    while openBrCount != 0:
        if expressionList[count+1] == "(":
            openBrCount += 1
        if expressionList[count+1] == ")":
            openBrCount -= 1
        count += 1

    length = len(expressionList[firstIndex+1:count])+1
    return length

def lenInClosedBracket(lastIndex, expressionList): 
#Function returns length of the items within brackets when a closed bracket is seen
    count = lastIndex
    closedBrCount = 1
    while closedBrCount != 0:
        if expressionList[count-1] == ")":
            closedBrCount += 1
        if expressionList[count-1] == "(":
            closedBrCount -= 1
        count -= 1

    length = len(expressionList[count+1:lastIndex])
    return length

def contentsClosedBracket(lastIndex, expressionList): 
#Function returns list of items within the brackets when a closed bracket is seen
    count = lastIndex
    closedBrCount = 1
    while closedBrCount != 0:
        if expressionList[count-1] == ")":
            closedBrCount += 1
        if expressionList[count-1] == "(":
            closedBrCount -= 1
        count -= 1

    newList = expressionList[count+1:lastIndex]
    return newList

def contentsOpenBracket(firstIndex, expressionList): 
#Function returns list of items within the brackets when an open bracket is seen
    count = firstIndex
    openBrCount = 1
    while openBrCount != 0:
        if expressionList[count+1] == "(":
            openBrCount += 1
        if expressionList[count+1] == ")":
            openBrCount -= 1
        count += 1

    newList = expressionList[firstIndex+1:count]
    return newList

def getNum(expressionList, countLocal): 
#Function returns the first and second numbers to operate on and the placement of those numbers in the overall list
    num1 = expressionList[countLocal-1]
    if  num1 == ")": #If either number is a bracket, the evaluate function is called 
                     #recursively to caclulate whatever is in the bracket
        length = lenInClosedBracket(countLocal-1, expressionList)
        num1 = evaluate(contentsClosedBracket(countLocal-1, expressionList))
        num1 = str(num1)
        num1 = list(num1)
        num1.remove("[")
        num1.remove("]")
        num1 = "".join(num1)
        expressionList[countLocal-1] = num1
        for x in range(length+1):
            del(expressionList[countLocal-2])
            countLocal -= 1
    num2 = expressionList[countLocal+1]
    if num2 == "(":
        length = lenInOpenBracket(countLocal+1, expressionList)
        num2 = evaluate(contentsOpenBracket(countLocal+1, expressionList))
        num2 = str(num2)
        num2 = list(num2)
        num2.remove("[")
        num2.remove("]")
        num2 = "".join(num2)
        expressionList[countLocal+1] = num2
        for x in range(length):
            del(expressionList[countLocal+2])
    
    return num1, num2, expressionList, countLocal

def evaluate(expression):
#Function turns string into a workable expression and when an operator is found, 
#the number in front and after are operated on based on the operator
    try:
        exprList = parseList(expression)
        count = -1
        while count < len(exprList)-2:
            count += 1
            if exprList[count] == "*":
                num1, num2, exprList, count = getNum(exprList, count)
                exprList[count-1] = float(num1) * float(num2)
                del(exprList[count])
                del(exprList[count])
                count -= 1
            elif exprList[count] == "/":
                num1, num2, exprList, count = getNum(exprList, count)
                exprList[count-1] = float(num1) / float(num2)
                del(exprList[count])
                del(exprList[count])
                count -= 1

        count = -1
        while count < len(exprList)-2:
            count += 1
            if exprList[count] == "+":
                num1, num2, exprList, count = getNum(exprList, count)
                exprList[count-1] = float(num1) + float(num2)
                del(exprList[count])
                del(exprList[count])
                count -= 1
            elif exprList[count] == "-":
                num1, num2, exprList, count = getNum(exprList, count)
                exprList[count-1] = float(num1) - float(num2)
                del(exprList[count])
                del(exprList[count])
                count -= 1

        return exprList
    except:
        return("MATH ERROR")

#MAIN PROGRAM

print("Welcome to the calculator program!")
print("")

while True: 
#Gets user input for the expression and error checks to make sure inputted expression is computable
    alist = []
    try:
        print("")
        num = input("Enter an expression (to exit, type \"done\"): ")
        print("")
        if num == "done":
            break
        evaluated = evaluate(num)
        x = 0
        while x<len(evaluated):
            try:
                evaluated[x] = float(evaluated[x])
                x+=1
            except:
                del evaluated[x]
        if len(evaluated) != 1:
            print("ERROR! Please try again!")
        else:
            print(evaluated[0]) #Outputs answer
        print("")
    except:
        print("ERROR! Please try again!")

print("Thank you for using the calculator program!")
