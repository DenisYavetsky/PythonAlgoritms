# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр

list_numbers = [int(i) for i in input('Введите числа и нажмите Enter').split()]


def sum_recurse(num, s=0):
    if num < 10:
        return s + num
    res = num % 10
    num = num // 10
    s += res
    return sum_recurse(num, s)


max_n = 0

for number in list_numbers:

    res = sum_recurse(number)
    if res > max_n:
        max_n = res
        n = number

print(f'Максимальное число по сумме цифр = {n}, его сумма = {max_n}')
