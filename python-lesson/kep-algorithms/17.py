def sum_of_digits(n):
    s = 0
    for ch in n:
        digit = int(ch)
        s += digit
    return s

for number in range(1000, 10000):
    if sum_of_digits(str(number)) % 2 == 0:
        print(number, end=' ')