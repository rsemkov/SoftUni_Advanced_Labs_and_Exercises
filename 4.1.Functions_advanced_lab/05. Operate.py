def operate(operator, *args):
    def add():
        return sum(args)

    def subtract():
        result = args[0]
        for el in args[1:]:
            result -= el
        return result

    def multiply():
        result = 1
        for el in args:
            result *= el
        return result

    def divide():
        result = args[0]
        for el in args[1:]:
            result /= el
        return result

    if operator == "+":
        return add()
    elif operator == "-":
        return subtract()
    elif operator == "*":
        return multiply()
    elif operator == "/":
        if 0 not in args[1:]:
            return divide()


print(operate("/", 20, 5, 2))



#OPTION 2:

# def operate(operator, *args):
#     result = ""
#     for num in args:
#         result += f"{num}{operator}"
#     return eval(result[:-1])
#
#
# print(operate("*", 3, 4))
