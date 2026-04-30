def calculate(number):
    s, p = 0, 1
    for digit in str(number):
        digit = int(digit)
        s += digit
        p *= digit

    return s, p

for n in range(100, 1000):
    s, p = calculate(n)
    if p % s == 0:
        print(n)