def concatenate(*args, **kwargs):
    result_string = ""
    for el in args:
        result_string += el

    for key, value in kwargs.items():
        result_string = result_string.replace(key, value)

    return result_string


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
