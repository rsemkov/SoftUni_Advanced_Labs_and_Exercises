def push(the_stack, the_number):
    the_stack.append(the_number)
    return the_stack


def delete(the_stack):
    if len(the_stack) > 0:
        the_stack.pop()
    return the_stack


def print_max(the_stack):
    if len(the_stack) > 0:
        print(max(the_stack))


def print_min(the_stack):
    if len(the_stack) > 0:
        print(min(the_stack))


def main():
    numbers_stack = []
    lines_count = int(input())
    for _ in range(lines_count):
        command = input()
        if command == "2":
            numbers_stack = delete(numbers_stack)
        elif command == "3":
            print_max(numbers_stack)
        elif command == "4":
            print_min(numbers_stack)
        else:  # command == "1"
            command = command.split()
            num = int(command[1])
            numbers_stack = push(numbers_stack, num)
    print(*numbers_stack[-1::-1], sep=", ")


main()
