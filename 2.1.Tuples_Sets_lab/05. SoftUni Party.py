def guests_collector(everyone):
    attending = set()
    while True:
        current_guest = input()
        if current_guest == "END":
            break
        attending.add(current_guest)

    missing = sorted(everyone.difference(attending))
    return missing


def main():
    guests_count = int(input())
    all_guests = {input() for _ in range(guests_count)}
    missing_guests = guests_collector(all_guests)
    printer(missing_guests)


def printer(missing):
    print(len(missing))
    print(*missing, sep="\n")


main()
