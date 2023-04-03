
def add(num1,num2):
    return num1+num2


def subtract(num1,num2):
    return num1-num2


def multiply(num1,num2):
    return num1*num2


def divide(num1,num2):
    return num1/num2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    more = True

    num1 = float(input('What is the first number?:'))

    for key in operations.keys():
        print(key)

    while more:
        operation = input('Pick a operator: ')
        num2 = float(input('What is the next number?: '))
        func = operations[operation]
        answer = func(num1, num2)
        print(answer)
        go = input(f'Type y to continue calculating with {answer}, or type n to start new calculation:  ')
        if go == 'n':
            more = False
            calculator()
        else:
            num1 = answer


calculator()