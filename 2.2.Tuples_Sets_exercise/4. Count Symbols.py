the_input = [_ for _ in input()]
elements_and_occurrences = {item: the_input.count(item) for item in the_input}

for element, occurrences in sorted(elements_and_occurrences.items()):
    print(f"{element}: {occurrences} time/s")
