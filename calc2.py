# A program to do simple math while demonstrating the use of Functions


def adding(num1, num2):
    answer = num1 + num2
    return answer


def subtracting(num1, num2):
    answer = int(num1) - int(num2)
    return answer


def multiplying(num1, num2):
    answer = int(num1) * int(num2)
    return answer


def dividing(num1, num2):
    answer = int(num1) / int(num2)
    return answer


num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Enter + - * / \n")

if operation == "+":
    answer = adding(num1, num2)

elif operation == "-":
    answer = subtracting(num1, num2)

elif operation == "*":
    answer = multiplying(num1, num2)

elif operation == "/":
    answer = dividing(num1, num2)


print("The result of " + str(num1) + " " + operation + " " + str(num2) + " = " + str(answer))



