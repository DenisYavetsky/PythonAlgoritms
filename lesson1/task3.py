# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки

x1, y1 = map(int, input('Введите координаты первой точки x1, y1 через пробел: ').split())
x2, y2 = map(int, input('Введите координаты второй точки x2, y2 через пробел: ').split())
if x1 == x2:
    print(f'Уравнение y = {x1}')
elif y1 == y2:
    print(f'Уравнение y = {y1}')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'Уравнение y = {k} * x + {b}')