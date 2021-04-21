# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
# сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.

OPERANDS = ('+', '-', '*', '/')

while True:
    znak = input('Введите операцию или 0 для выхода: ')
    if znak == '0':
        break
    if znak in OPERANDS:

        a, b = input('Введите 2 числа через пробел: ').split()
        execute_str = a + znak + b
        if znak == '/' and int(b) == 0:
            print('Деление на ноль')
        else:
            print(eval(execute_str))
    else:
        print('Операция не распознана. Повторите ввод')
