# Найти сумму и произведение цифр трехзначного числа

abc = int(input('Введите трехзначное число: '))

a = abc // 100
c = abc % 10
b = (abc % 100) // 10
print(f'Сумма = {a + b + c}')
print(f'Произведение = {a * b * c}')
