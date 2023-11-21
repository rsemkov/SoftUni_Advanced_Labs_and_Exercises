def even_odd_filter(**kwargs):
    for key, value in kwargs.items():
        if key == "even":
            kwargs[key] = [el for el in value if el % 2 == 0]
        else:
            kwargs[key] = [el for el in value if el % 2 != 0]

    sorted_values = sorted(kwargs.items(), key=lambda x: -len(x[1]))
    sorted_dict = {}
    for key, value in sorted_values:
        sorted_dict[key] = value

    return sorted_dict


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
