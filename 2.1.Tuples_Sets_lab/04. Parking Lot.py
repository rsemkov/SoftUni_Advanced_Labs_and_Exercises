def parking_manager(n):
    the_set = set()
    for _ in range(n):
        command, car_plate = input().split(", ")
        if command == "IN":
            the_set.add(car_plate)
        elif command == "OUT":
            the_set.remove(car_plate)
    return the_set


def printer(the_set):
    if the_set:
        print(*the_set, sep="\n")
    else:
        print("Parking Lot is Empty")


def main():
    operations_counter = int(input())
    cars_set = parking_manager(operations_counter)
    printer(cars_set)


main()
