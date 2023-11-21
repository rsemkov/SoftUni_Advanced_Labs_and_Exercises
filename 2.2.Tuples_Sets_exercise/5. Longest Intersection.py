n = int(input())
longest_intersection = None
longest_intersection_len = 0

for _ in range(n):
    first_part, second_part = input().split("-")
    begin_first, end_first = [int(_) for _ in first_part.split(",")]
    begin_second, end_second = [int(_) for _ in second_part.split(",")]

    # create 2 sets and calculate their intersection:
    first_set = {_ for _ in range(begin_first, end_first + 1)}
    second_set = {_ for _ in range(begin_second, end_second + 1)}
    current_intersection = first_set.intersection(second_set)

    # check if the current intersection is the biggest one so far:
    if len(current_intersection) > longest_intersection_len:
        longest_intersection = current_intersection
        longest_intersection_len = len(current_intersection)

print(f"Longest intersection is {list(longest_intersection)} with length {longest_intersection_len}")
