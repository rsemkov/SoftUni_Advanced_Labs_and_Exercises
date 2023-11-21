deliveries_stack = list(map(int, input().split()))
capacity_per_rack = int(input())

racks_used_counter = 1
current_rack = 0
while deliveries_stack:
    current_item = deliveries_stack.pop()
    if current_item + current_rack > capacity_per_rack:
        racks_used_counter += 1
        current_rack = 0

    current_rack += current_item

print(racks_used_counter)






