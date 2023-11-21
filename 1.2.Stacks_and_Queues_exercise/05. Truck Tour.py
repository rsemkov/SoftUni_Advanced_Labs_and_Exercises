from collections import deque
circles_count = int(input())
trips_to_complete = deque()
for _ in range(circles_count):
    trips_to_complete.append(list(map(int, input().split())))

counter = 0
for _ in range(circles_count):
    current_fuel = 0
    for trip in trips_to_complete:
        fuel_loaded = trip[0]
        fuel_needed = trip[1]
        current_fuel += fuel_loaded
        if current_fuel >= fuel_needed:
            current_fuel -= trip[1]
            continue
        trips_to_complete.append(trips_to_complete.popleft())
        counter += 1
        break
print(counter)


# WITH FUNCTIONS:
# from collections import deque
#
#
# def trips_generator(the_circles):
#     trips_to_complete = deque()
#     for _ in range(the_circles):
#         trips_to_complete.append(list(map(int, input().split())))
#     return trips_to_complete
#
#
# def trips_execute(the_circles, the_trips):
#     counter = 0
#     for _ in range(the_circles):
#         current_fuel = 0
#         for trip in the_trips:
#             fuel_loaded = trip[0]
#             fuel_needed = trip[1]
#             current_fuel += fuel_loaded
#             if current_fuel >= fuel_needed:
#                 current_fuel -= trip[1]
#                 continue
#             the_trips.append(the_trips.popleft())
#             counter += 1
#             break
#     return counter
#
#
# def main():
#     circles_count = int(input())
#     trips = trips_generator(circles_count)
#     print(trips_execute(circles_count, trips))
#
#
# main()
