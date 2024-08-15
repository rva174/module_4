def true_divide(first, second):
    import math
    math.inf

    if second > 0:
        return first / second
    if second == 0:
        return math.inf

result1 = true_divide(69, 3)
result2 = true_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)

