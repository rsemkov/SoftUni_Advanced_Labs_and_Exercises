n, m = [int(x) for x in input().split()]
set_n = {input() for _ in range(n)}
set_m = {input() for _ in range(m)}
reoccurring_nums = set_m.intersection(set_n)

print(*reoccurring_nums, sep="\n")
