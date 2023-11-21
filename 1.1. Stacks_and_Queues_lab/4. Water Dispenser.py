from collections import deque
water_quantity = int(input())
people_queue = deque()

while True:
    person = input()
    if person == "Start":
        break
    people_queue.append(person)

while True:
    command = input()
    if command == "End":
        break
    if command.isdigit():
        litres_needed = int(command)
        person_name = people_queue.popleft()
        if litres_needed <= water_quantity:
            water_quantity -= litres_needed
            print(f"{person_name} got water")
        else:
            print(f"{person_name} must wait")
    else:
        command = command.split()
        added_litres = int(command[1])
        water_quantity += added_litres

print(f"{water_quantity} liters left")
