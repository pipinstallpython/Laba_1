import math
# площадь треугольника
lst = list(map(int, input("Введите строны треугольника ").split()))
p = sum(list) / 2
S_triangle = math.sqrt(p * (p - lst[0]) * (p - lst[1]) * (p - lst[2]))
print(S_triangle)

# площадь круга
r = int(input("Введите радиус круга "))
S_circle = math.pi * r**2
print(S_circle)

# площадь прямоугольника
a, b = map(int, input("Введите стороны прямоугольника ").split())
S_rectangle = a * b
print(S_rectangle)

# объем конуса
R, H = map(int, input("Введите радиус основания и высоту конуса ").split())
V_conus = 1/3 * (math.pi * R**2 * H)
print(V_conus)


