import math

# площадь треугольника
def triangle():
    lst = list(map(int, input("Введите строны треугольника: ").split()))
    p = sum(list) / 2
    S_triangle = math.sqrt(p * (p - lst[0]) * (p - lst[1]) * (p - lst[2]))
    return S_triangle

# площадь круга
def circle():
    r = int(input("Введите радиус круга: "))
    S_circle = math.pi * r**2
    return S_circle

# площадь прямоугольника
def rectangle():
    a, b = map(int, input("Введите стороны прямоугольника: ").split())
    S_rectangle = a * b
    return S_rectangle

# объем конуса
def conus():
    R, H = map(int, input("Введите радиус основания и высоту конуса: ").split())
    V_conus = 1/3 * (math.pi * R**2 * H)
    return V_conus

figure = input("Площадь/объем какой фигуры нужно поставить(треугольник, круг, прямоугольник, конус): ")

if figure == 'треугольник':
    print(triangle())
elif figure == 'круг':
    print(circle())
elif figure == 'прямоугольник':
    print(rectangle())
elif figure == 'конус':
    print(conus())
else: print('error')


