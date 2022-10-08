# площадь треугольника
a, b, c = map(int, input().split())
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(S)


