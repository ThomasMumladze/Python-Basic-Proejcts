def __userName (name):
    return ("Hello " + name)

def __result(result):
    return ("Your Result is " + str(result))

def __calculator (numOne , operation , numTwo):
    for i in operation:
        if i == " ":
            continue
        if i == "*":
            return numOne * numTwo
        elif i == "/":
                return numOne / numTwo
        elif i == "+":
            return numOne + numTwo
        elif i == "-":
            return numOne - numTwo

def __MAIN():
    userName = input("Enter your Name: ")
    firstNumber = float(input("Enter First Number: "))
    operation = input("Enter Operation: * / + - : ")
    secondNumber = float(input('Enter Second Number: '))
    
    print(__userName(userName))
    result = __calculator(operation=operation , numOne= firstNumber , numTwo=secondNumber)
    print(__result(result))  
    
__MAIN();