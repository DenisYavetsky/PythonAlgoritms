# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

a, b, c = map(int, input('Введите три разных числа через пробел: ').split())

average = a
if a > b:
    if b > c:
        average = b
    elif a > c:
        average = c
else:
    if c > b:
        average = b
    elif a < c:
        average = c
print(f'Среднее - {average}')


def test(a, b, c):
    average = a
    if a > b:
        if b > c:
            average = b
        elif a > c:
            average = c
    else:
        if c > b:
            average = b
        elif a < c:
            average = c
    return average


assert test(1, 2, 3) == 2
assert test(1, 3, 2) == 2
assert test(2, 1, 3) == 2
assert test(2, 3, 1) == 2
assert test(3, 1, 2) == 2
assert test(3, 2, 1) == 2
