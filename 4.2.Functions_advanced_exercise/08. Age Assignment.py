def age_assignment(*args, **kwargs):
    results_dict = {}
    final_result = ""
    for name in args:
        if name[0] in kwargs.keys():
            results_dict[name] = kwargs[name[0]]

    sorted_names_ages = sorted(results_dict.items())

    for name, age in sorted_names_ages:
        final_result += f"{name} is {age} years old.\n"

    return final_result


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

