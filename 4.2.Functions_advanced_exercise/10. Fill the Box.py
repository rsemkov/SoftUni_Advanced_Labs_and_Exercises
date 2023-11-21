def fill_the_box(*args):
    height, length, width = args[:3]
    box_size = height * length * width

    finish_idx = args.index("Finish")
    total_cubes = sum(args[3:finish_idx])

    if box_size - total_cubes > 0:
        return f"There is free space in the box. You could put {box_size - total_cubes} more cubes."
    return f"No more free space! You have {total_cubes - box_size} more cubes."


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
