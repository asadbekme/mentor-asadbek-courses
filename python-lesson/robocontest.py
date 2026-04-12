# 1-masala
# a = int(input())
# b = int(input())
# print(a+b)

# Fibonichchi sonlar: o'zidan oldingi 2 ta sonni qo'shish orqali hosil bo'ladi
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

# 2-masala
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, a + b
    return b

n = int(input())
print(fibonacci(n))
