n = int(input())
odd_set = set()
even_set = set()
for current_row in range(1, n + 1):
    current_name = input()
    current_sum = sum(ord(letter) for letter in current_name)
    current_result = int(current_sum / current_row)

    if current_result % 2 == 0:
        even_set.add(current_result)
    else:
        odd_set.add(current_result)

if sum(even_set) > sum(odd_set):
    print(*odd_set.symmetric_difference(even_set), sep=", ")
elif sum(even_set) < sum(odd_set):
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.union(even_set), sep=", ")
