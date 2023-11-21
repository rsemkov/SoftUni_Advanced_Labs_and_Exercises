nums_list = list(map(int, input().split()))
positives_sum = sum(x for x in nums_list if x > 0)
negatives_sum = sum(y for y in nums_list if y < 0)

print(negatives_sum)
print(positives_sum)
if abs(negatives_sum) > positives_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
