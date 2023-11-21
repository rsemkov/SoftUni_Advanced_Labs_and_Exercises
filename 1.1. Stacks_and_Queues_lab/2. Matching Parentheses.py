str_input = input()

opening_parentheses_indices = []
for index, item in enumerate(str_input):
    if item == "(":
        opening_parentheses_indices.append(index)
    elif item == ")":
        starting_index = opening_parentheses_indices.pop()
        print(str_input[starting_index:index + 1])
