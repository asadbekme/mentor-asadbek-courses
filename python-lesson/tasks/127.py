def calculate(a, b):
    s = 0
    for i in range(a, b + 1):
        s += i
    return s

print(calculate(1, 5))  # 15 (1+2+3+4+5)
print(calculate(3, 7))  # 25 (3+4+5+6+7)