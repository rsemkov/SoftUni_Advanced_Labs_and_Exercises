from collections import deque
food_quantity = int(input())
people_in_line = deque(int(x) for x in input().split())
print(max(people_in_line))

everyone_served = True
while people_in_line:
    if people_in_line[0] <= food_quantity:
        food_served = people_in_line.popleft()
        food_quantity -= food_served
    else:
        everyone_served = False
        break

if everyone_served:
    print("Orders complete")
else:
    print("Orders left:", *people_in_line, sep=" ")

