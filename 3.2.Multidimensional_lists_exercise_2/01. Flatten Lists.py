the_input = input().split("|")
for el in the_input[-1::-1]:
    el = [_ for _ in el.split()]
    for item in el:
        print(item, end=" ")
