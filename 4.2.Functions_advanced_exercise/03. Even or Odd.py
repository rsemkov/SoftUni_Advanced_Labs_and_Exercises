def even_odd(*args):
    if args[-1] == "even":
        filtered_list = [el for el in args[:-1] if el % 2 == 0]
    else:
        filtered_list = [el for el in args[:-1] if el % 2 != 0]
    return filtered_list


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
