# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, то надо вывести число 6843

num = int(input('Введите целое число: '))


def num_recurse(num, s=0):
    if num < 10:
        return s * 10 + num
    res = num % 10
    num = num // 10
    s = s * 10 + res
    return num_recurse(num, s)


print(num_recurse(num))
