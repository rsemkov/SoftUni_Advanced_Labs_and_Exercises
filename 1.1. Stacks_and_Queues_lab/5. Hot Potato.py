from collections import deque
participants = deque(input().split())
hot_potato = int(input())

counter = 1
while len(participants) > 1:
    current_kid = participants.popleft()
    if counter == hot_potato:
        counter = 1
        print(f"Removed {current_kid}")
    else:
        participants.append(current_kid)
        counter += 1

print(f"Last is {' '.join(participants)}")
