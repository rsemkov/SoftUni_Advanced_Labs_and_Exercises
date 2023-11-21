n = int(input())
unique_users = {input() for _ in range(n)}   # THIS IS SET COMPREHENSION
print(*unique_users, sep="\n")
