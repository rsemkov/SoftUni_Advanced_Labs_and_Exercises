def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""
    for key, value in sorted_cheeses:
        sorted_value = sorted(value, reverse=True)
        sorted_value = '\n'.join([str(x) for x in sorted_value])
        result += f"{key}\n{sorted_value}\n"
    return result


print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)