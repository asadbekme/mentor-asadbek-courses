import math
a = int(input())
b = int(input())
D = a * a - 4 * b
sqrt_D = math.sqrt(D)
x1 = (a - sqrt_D) / 2
x2 = (a + sqrt_D) / 2
if D == int(sqrt_D) ** 2:  # D kvadrat son bo'lsa, ildizlar butun son bo'ladi
    x1 = int(x1)
    x2 = int(x2)

print(x1, x2)