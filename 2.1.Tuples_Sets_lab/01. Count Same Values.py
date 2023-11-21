nums_input = [float(x) for x in input().split()]
nums_dict = {value: nums_input.count(value) for value in nums_input}

for number, count in nums_dict.items():
    print(f"{number:.1f} - {count} times")
