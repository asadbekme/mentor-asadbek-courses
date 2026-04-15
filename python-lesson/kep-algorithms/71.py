def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

n = input()
n1 = n[0:3]
n2 = n[3:6]
print(sum_of_digits(n1) == sum_of_digits(n2))