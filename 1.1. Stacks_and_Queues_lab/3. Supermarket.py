from collections import deque
people_queue = deque()
while True:
    person = input()
    if person == "Paid":
        while people_queue:
            person_leaving = people_queue.popleft()
            print(person_leaving)
    elif person == "End":
        print(f"{len(people_queue)} people remaining.")
        break
    else:
        people_queue.append(person)
