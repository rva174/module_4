def fake_divide(first, second):
    if second > 0:
       return first / second
    if second <= 0:
       return 'Ошибка'

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = fake_divide(49, 7)
result4 = fake_divide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)

