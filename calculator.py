import math
# площадь треугольника
a, b, c = map(int, input("Введите строны треугольника ").split())
p = (a + b + c) / 2
S_abc = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(S_abc)

# площадь круга
r = int(input("Введите радиус круга "))
S_r = math.pi * r**2
print(S_r)

